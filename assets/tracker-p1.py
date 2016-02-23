
#!/usr/bin/env python

"""Simple TRACKER server application for use in cs457p2p Part 1"""

import socket
import pickle

#  server host (local machine)
host = 'localhost' 

#  machine port
port = 7777

#  number of requests before need to thread...
backlog = 5

#  max length of data buffer (bytes) 
size = 1024

#  create a socket
#    AF_INET = ipv4 addressing 
#    SOCK_STREAM = transport protocol (tcp)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#  bind the socket to machine and port
s.bind((host,port)) 

#  listen on socket
s.listen(backlog)

db = [(12, 'of'), (3, 'time'), (9, 'review'), (6, 'good'), (2, 'the'), (5, 'all'), (11, 'use'), (8, 'to'), (1, 'is'), (7, 'coders'), (14, 'in'), (15, 'python.'), (10, 'the'), (0, 'Now'), (4, 'for'), (13, 'threads')]


#  poll for connections
try:

    while 1:
        try:
            client, address = s.accept() # returns a tuple representing connection
            print 'Message from', address
            data = client.recv(size) # reads in the payload
            
            if data == 'REGISTER':
                serialized_data = pickle.dumps(len(db))
                client.send(serialized_data)
                client.close()
            else:
                try:
                    deserialized_data = pickle.loads(data)
                    serialized_data = pickle.dumps(db[deserialized_data])
                    client.send(serialized_data) # sends it back
                except:
                    client.send(pickle.dumps('Bad request'))

            client.close() # close the connection

        except:
            s.close()

except KeyboardInterrupt:
    s.close()
