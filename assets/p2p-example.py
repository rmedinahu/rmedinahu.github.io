""" python thread example """

import threading
import time
import socket
import pickle

DB_MAG = 0
ASSEMBLED_DB = []

#  server host (local machine)
host = 'localhost' 

#  machine port
port = 7777

#  number of requests before need to thread...
backlog = 5

#  max length of data buffer (bytes) 
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

class ServerThread(threading.Thread):
    def __init__(self, threadID, name, e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.runtime = e


    def run(self):
        print "Starting " + self.name
        server_proc(self.runtime)

class ClientThread(threading.Thread):
    def __init__(self, threadID, name, e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.runtime = e

    def run(self):
        print "Starting " + self.name   
        client_proc(self.runtime)

def server_proc(runtime):
    global ASSEMBLED_DB, DB_MAG, s, host, port, backlog, size
    s.bind((host,port)) 
    
    #  listen on socket
    s.listen(backlog)

    while runtime.is_set(): 
        try:
            while 1:
                client, address = s.accept()  # returns a tuple representing connection
                print 'Message from', address[0]
                data = client.recv(size)  # reads in the packet
                print 'DATA=>', data
                client.send('SERVER SAYS: ' + data)

                data_in = pickle.loads(data)  # deserializes packet to tuple

                client.close() # close the connection

        except KeyboardInterrupt:
            s.close()
            runtime.clear()

        except Exception as e:
            s.close()
            runtime.clear()
       

def client_proc(runtime):
    global host, port, size
    try:
        i = 0
        while i < 20:
            lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

            lsock.connect((host, port))
            lsock.send('HELLO')
            response = lsock.recv(size)
            print response
            i += 1
        
        
    except Exception as e: 
        print e
    s.close()





       

""" SETUP """

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
# allowing the threads to exit cleanly, then end the program.
try:
    while 1:
        pass

except KeyboardInterrupt:
    
    print "\nAttempting to close threads."
    runtime_e.clear()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print "\n All threads closed."

print "Exiting Main Thread"