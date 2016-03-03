"""p2p tracker application"""

import socket
import pickle
import time
import threading

from collections import OrderedDict


#  server host (local machine)
host = '10.7.210.108' 

#  machine port
port = 7777

#  number of requests before need to thread...
backlog = 5

#  max length of data buffer (bytes) 
size = 1024

#  create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#  bind the socket to machine and port
s.bind((host,port)) 

#  listen on socket
s.listen(backlog)

db = [(4, 'peaks'), (2, 'and'), (0, 'blue'), (3, 'snowy'), (1, 'skies')]

peers = []  # A peer is a tuple: (str_handle, str_ip_addr, int_port_num)


class UpdaterThread(threading.Thread):
    def __init__(self, e):
        threading.Thread.__init__(self)
        self.runtime = e

    def run(self):
        print "Starting Updater..."
        while self.runtime.is_set():
            time.sleep(20)
            prune_peers()

def get_nbr_peer(peer):
    global peers
    
    cur = peers.index( (peer[0], peer[1], peer[2]) )
    return peers[ (cur-1) % len(peers)]

def get_peer_by_handle(peer_handle):
    global peers
    
    for i in peers:
        if i[0] == peer_handle:
            return i
    return None

def add_peer(peer_handle, peer_ip, peer_port_num):
    global peers
    
    if not get_peer_by_handle(peer_handle):
        p = (peer_handle, peer_ip, peer_port_num)
        peers.append(p)
        return p
    
    return None

def prune_peers():
    global peers, size

    updated_peers = []
    num_peers = len(peers)

    for i in range(num_peers):
        handle, ip_addr, port = peers[i][0], peers[i][1], peers[i][2]
        try:
            ping_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ping_socket.settimeout(5)
            ping_socket.connect((ip_addr, port))
            packet = ('PING', time.asctime())
            ping_socket.send( pickle.dumps(packet) )
            
            response = ping_socket.recv(size)
            
            updated_peers.append(peers[i])
            ping_socket.close()

        except Exception as e:
            # Request timed out. Current peer not added to updated list (will be removed).
            print e
            ping_socket.close()
            print '\n==> REMOVED', handle, '@', ip_addr, port

            continue

    if len(updated_peers) < num_peers:
        peers = updated_peers
        update_nbrs()

def update_nbrs():
    global peers
    num_peers = len(peers)

    if num_peers < 2:
        return  # Only one peer. One is a lonely number...   

    # Send update message to each peer with info for neighbor
    for i in range(num_peers): 
        handle, ip_addr, port = peers[i][0], peers[i][1], peers[i][2]
        nbr = peers[(i - 1) % num_peers]
        nbr_handle, nbr_ip_addr, nbr_port = nbr[0], nbr[1], nbr[2]

        try:
            
            update_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            update_socket.settimeout(2)
            update_socket.connect((ip_addr, port))
            packet = ('UPDATE_NBR', nbr_handle, nbr_ip_addr, nbr_port)
            update_socket.send(pickle.dumps(packet))
            update_socket.close()
            # Not waiting for response...
        except:
            pass
            continue


# Main Execution ...

threadLock = threading.Lock()
runtime_e = threading.Event()
runtime_e.set()
updater = UpdaterThread(runtime_e)
updater.start()



#  poll for connections
try:
    print 'Tracker listening at', host, '@', port
    while 1:
        try:
            client, address = s.accept()  # returns a tuple representing connection
            print 'Message from', address[0]
            data = client.recv(size)  # reads in the packet
            data_in = pickle.loads(data)  # deserializes packet to tuple
            request = data_in[0]
            print data_in
            
            if request == 'REGISTER':
                nbr = (None, None, None)
                new_peer = add_peer(data_in[1], address[0], data_in[2]) # log the registration
                
                if new_peer:
                    print 'Registration logged:', peers
                    nbr = get_nbr_peer(new_peer)
                    if not nbr:
                        nbr = (None, None, None)

                    hash_like = peers.index(new_peer)
                    dbitem = db[ hash_like%len(db) ]                

                packet = ('REG_INIT', nbr[0], nbr[1], nbr[2], len(db), dbitem)
                client.send(pickle.dumps(packet))
                
                update_nbrs()

            elif request == 'ECHO':
                msg = 'Hi ' + data_in[1] + ', Welcome to the network. Register to get started.'
                packet = ('[Tracker]', msg)
                client.send(pickle.dumps(packet))

            else:
                packet = ('[Tracker]', 'Bad request')
                client.send(pickle.dumps(packet))

            client.close() # close the connection 

        except KeyboardInterrupt:
            s.close()
            runtime_e.clear()
            break

        except Exception as e:
            print e
            s.close()

except KeyboardInterrupt:
    s.close()
    runtime_e.clear()


