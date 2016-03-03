""" python thread example """

import threading
import time
import socket
import pickle

BACKLOG = 5
BUFFER_SIZE = 1024

TRACKER_CONNECTION = ()
MYSERVER_CONNECTION = ()
NEIGHBOR_CONNECTION = ()

MYHANDLE = ''
DB = {}
DB_LEN = 0


def get_next_item():
    """ Helper function to determine next item needed. Use if you want."""
    for i in range(DB_LEN):
        if i not in DB:
            return i
    return -1 

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
            # Set up server thread to accept requests from peers. Remove sleep in your implementation.
            # Review the protocol to understand which requests you need to handle!
            time.sleep(1)

        except Exception as e:
            print 'Server Error==> ' + str(e)
            runtime.clear()
          
       
def client_proc(runtime):
    global BACKLOG, BUFFER_SIZE, TRACKER_CONNECTION, MYSERVER_CONNECTION, NEIGHBOR_CONNECTION, MYHANDLE, DB, DB_LEN
    
    try:
        # SANITY CHECK. CAN YOU REACH THE TRACKER?
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(TRACKER_CONNECTION)
        
        packet = ('ECHO', MYHANDLE)
        packet = pickle.dumps(packet) # Serialize request
        
        client_socket.send(packet) 

        response = client_socket.recv(BUFFER_SIZE)
        response = pickle.loads(response) # Deserialize response

        client_socket.close()

        print response[0], ' ==> ', response[1]

        # REGISTER WITH TRACKER...

        # IF REGISTRATION COMPLETED WITHOUT ERROR, BEGIN GATHERING DB ITEMS. SEE PROTOCOL!      
        
        seq = get_next_item()

        while seq > -1:
            try:
                # YOUR QUERY REQUESTS ARE HERE 
                time.sleep(2)
            except:
                continue # Keep requesting until DB is complete

    except Exception as e: 
        print 'Client Error ==> ' + str(e)
        print 'Tracker server not available or other error in client.'
        client_socket.close()
        runtime.clear()


""" SETUP """

port = raw_input("ENTER THE PORT TO LISTEN ON (9000 is default):")
host = raw_input("ENTER THE HOST TO LISTEN ON (localhost is default):")

if not host: host='localhost'
if not port: port=9000
else: port=int(port)

hndl = raw_input("ENTER YOUR HANDLE (nickname):")
trkr = raw_input("ENTER IP OF TRACKER (localhost is default):")
if not trkr: host='localhost'

TRACKER_CONNECTION = (trkr, 7777)
MYSERVER_CONNECTION = (host, port)
MYHANDLE = hndl

# Create the socket for server thread
MYSERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MYSERVER_SOCKET.bind(MYSERVER_CONNECTION) 
MYSERVER_SOCKET.listen(BACKLOG)

# Manage the server thread process
runtime_e = threading.Event()
runtime_e.set()

# Create new threads
server = ServerThread(1, "Server", runtime_e)
client = ClientThread(2, "Client", runtime_e)

# Start new Threads
server.start()
time.sleep(2)
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