""" python p2p dht example """

import threading
import time
import socket
import pickle

BACKLOG = 5
BUFFER_SIZE = 1024
TRACKER_CONNECTION = ('localhost', 7777)

MYSERVER_CONNECTION = ()
NEIGHBOR_CONNECTION = () #(NBR_HANDLE, NBR_HOST, NBR_PORT)
MYHANDLE = ''
DB = {}
DB_LEN = 0



class ServerThread(threading.Thread):
    def __init__(self, threadID, name, e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.runtime = e

    def run(self):
        print "Starting My " + self.name
        server_proc(self.runtime)

class ClientThread(threading.Thread):
    def __init__(self, threadID, name, e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.runtime = e

    def run(self):
        print "Starting My " + self.name   
        client_proc(self.runtime)

def server_proc(runtime):
    global BUFFER_SIZE, MYSERVER_SOCKET, NEIGHBOR_CONNECTION, MYHANDLE, DB
 
    while runtime.is_set():
        try:
            requestor, address = MYSERVER_SOCKET.accept()   # blocks waiting for a tuple representing connection
            data = requestor.recv(BUFFER_SIZE)              # read in the data
            data = pickle.loads(data)                       # deserialize packet
            request = data[0]                               # read REQUEST command from packet
            if request == 'UPDATE_NBR':
                new_nbr = (data[1], data[2], data[3])
                if new_nbr != NEIGHBOR_CONNECTION:
                    NEIGHBOR_CONNECTION = new_nbr
                    print '[', MYHANDLE, ']', 'NEW NEIGHBOR ==>', NEIGHBOR_CONNECTION
            
            elif request == 'PING':
                print '[', MYHANDLE, ']', 'Received ping!'
                packet = ('ACK', MYHANDLE)
                requestor.send(pickle.dumps(packet))
            
            elif request == 'QUERY':
                dbkey = int(data[1])
                
                try:
                    dbitem = (dbkey, DB[dbkey])

                except Exception as e:
                    print '[', MYHANDLE, ']', dbkey, 'Current db ==>', DB
                    dbitem = (None, None) 

                packet = ('QUERY_RESULT', dbitem)
                requestor.send(pickle.dumps(packet))
            
            else:
                requestor.send('No data sent!')
            
            requestor.close() # close the connection

        except Exception as e:
            print 'Server Error==> ' + str(e)
            runtime.clear()

def get_next_item():
    for i in range(DB_LEN):
        if i not in DB:
            return i

    return -1           
       
def client_proc(runtime):
    global BACKLOG, BUFFER_SIZE, TRACKER_CONNECTION, MYSERVER_CONNECTION, NEIGHBOR_CONNECTION, MYHANDLE, DB, DB_LEN
    
    try:
        # REGISTER WITH TRACKER
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(TRACKER_CONNECTION)
        
        message = ('REGISTER', MYHANDLE, MYSERVER_CONNECTION[1]) # SEND PORT NUMBER WITH HANDLE
        client_socket.send(pickle.dumps(message))
        
        data = pickle.loads(client_socket.recv(BUFFER_SIZE))
    
        client_socket.close()

        if data:
            print 'Registered with ==>', data
            try:
                nbr = (data[1], data[2], data[3])
                dbsize = data[4]
                dbpakt = data[5]
            except:
                return 'Bad registration.'

            NEIGHBOR_CONNECTION=nbr
            DB_LEN = dbsize
            DB[dbpakt[0]] = dbpakt[1]

        else:
            return 'Bad registration.'

        print '\nREGISTERED AND READY!\n'      
        
        seq = get_next_item()

        while seq > -1:
            try:
                time.sleep(2)
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((NEIGHBOR_CONNECTION[1], NEIGHBOR_CONNECTION[2]))
                
                
                packet = ('QUERY', seq)            
                client_socket.send(pickle.dumps(packet))
                
                data = client_socket.recv(BUFFER_SIZE)
                data = pickle.loads(data)

                if data[0] == 'QUERY_RESULT':
                    dbitem = data[1]
                    key, item = dbitem[0], dbitem[1]
                    
                    if key >= 0:
                        if key not in DB:
                            DB[key] = item
                            print '[', MYHANDLE, ']', 'FROM', NEIGHBOR_CONNECTION[0], '*****', DB, '*****'
                            seq = get_next_item()
                            print '[', MYHANDLE, ']', 'Now Querying ', NEIGHBOR_CONNECTION[0], 'for', str(seq)
                
                client_socket.close()
            
            except:
                continue

    except Exception as e: 
        print 'Client Error ==> ' + str(e)
        client_socket.close()
        runtime.clear()
    
""" SETUP """
hndl = raw_input("ENTER YOUR HANDLE:")
port = raw_input("ENTER THE PORT TO LISTEN ON:")
host = raw_input("ENTER THE HOST TO LISTEN ON:")
if not host: host='localhost'
if not port: port=9000
else: port=int(port)

TRACKER_CONNECTION = ('localhost', 7777)
MYSERVER_CONNECTION = (host, port)
MYHANDLE = hndl

MYSERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MYSERVER_SOCKET.bind(MYSERVER_CONNECTION) 
MYSERVER_SOCKET.listen(BACKLOG)

threadLock = threading.Lock()
runtime_e = threading.Event()
runtime_e.set()

# Create new threads
server = ServerThread(1, "Server", runtime_e)
client = ClientThread(2, "Client", runtime_e)

# Start new Threads
server.start()
time.sleep(3)
client.start()

# Add threads to thread list
threads = []
threads.append(server)
threads.append(client)


# Monitor the main thread listening for CTRL-C which will unset the runtime flag then 
# allow the threads to exit cleanly, then end the program.
try:
    while 1:
        time.sleep(1)

except KeyboardInterrupt:
    print "\nAttempting to close threads."
    runtime_e.clear()
    kill_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    kill_socket.connect(MYSERVER_CONNECTION)
    kill_socket.send('EXIT!')

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print "\nAll threads closed."

print "Exiting Main Thread"