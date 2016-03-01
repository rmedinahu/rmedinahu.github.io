""" python thread example """

import threading
import time
import socket
import pickle

BACKLOG = 5
BUFFER_SIZE = 1024
MYSERVER_CONNECTION = ()


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
    global BACKLOG, BUFFER_SIZE, MYSERVER_CONNECTION

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind(MYSERVER_CONNECTION) 
    server_socket.listen(BACKLOG)

    while runtime.is_set():
        try:
            client, address = server_socket.accept()  # blocks waiting for a tuple representing connection
            data = client.recv(BUFFER_SIZE)  # reads in the packet

            if data:
                client.send('Echo Server ==> ' + data)
            else:
                client.send('Echo Server ==> No data sent!')
            
            client.close() # close the connection
        
        except KeyboardInterrupt:
            print "\nAttempting to close server."
            runtime.clear()

        except Exception as e:
            print 'Server Error ==> ' + str(e)
    
    
    server_socket.close()
    
       
def client_proc(runtime):
    global BACKLOG, BUFFER_SIZE, TRACKER_CONNECTION, MYSERVER_CONNECTION, NEIGHBOR_CONNECTION, MYHANDLE, DB, DB_LEN
    
    try:
        counter = 0
        while counter < 5:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(MYSERVER_CONNECTION)
            client_socket.send(str(counter) + ' -- Hi thread buddy!')
            response = client_socket.recv(BUFFER_SIZE)
            print response
            client_socket.close()
            time.sleep(2)
            counter += 1        

        runtime.clear()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(MYSERVER_CONNECTION)
        client_socket.send('Bye!')
        response = client_socket.recv(BUFFER_SIZE)
        print response

    except Exception as e: 
        print 'Client Error ==> ' + str(e)
        client_socket.close()
        runtime.clear()




""" SETUP """

port = int(raw_input("ENTER THE PORT TO LISTEN ON:"))
host = raw_input("ENTER THE HOST TO LISTEN ON:")
MYSERVER_CONNECTION = (host, port)

threadLock = threading.Lock()
runtime_e = threading.Event()
runtime_e.set()

# Create new threads
server = ServerThread(1, "Server", runtime_e)
client = ClientThread(2, "Client", runtime_e)

# Start new Threads
server.start()
time.sleep(3) # Wait for server to initialize
client.start()

# Add threads to thread list
threads = []
threads.append(server)
threads.append(client)


# Monitor the main thread listening for CTRL-C which will unset the runtime flag then 
# allow the threads to exit cleanly, then end the program.
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