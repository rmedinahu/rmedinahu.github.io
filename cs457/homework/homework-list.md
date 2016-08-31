---
layout: course_page
title: 
permalink: /457/hw/
parent_course: 457
---
> [hw-14 due may 2 @ 11am](#hw-14)(has solution)

> [hw-13 due apr 28 @ 11am](#hw-13)(has solution)

> [hw-12 due apr 18 @ 5pm](#hw-12)(has solution)

> [hw-11 due apr 8 @ 5pm](#hw-11)(has solution)

> [hw-10 due apr 1 @ 5pm](#hw-10)(has solution)

\* [hw-09 due mar 14 @ 5pm](#hw-09) (has solution)

\* [hw-08 due feb 25 @ 5pm](#hw-08)

\* [hw-07 due feb 18 @ 5pm](#hw-07)

\* [hw-06 due feb 17 @ 5pm](#hw-06) (has solution)

\* [hw-05 due feb 10](#hw-05) (has solution)

\* [hw-04 due feb 05](#hw-04)

\* [hw-03 due feb 02](#hw-03)

\* [hw-02 due jan 28](#hw-02)

\* [hw-01 due jan 26](#hw-01)

\* **graded**


HW 01
---

----

Jan 21

* Read chapter 1 sections 1.1 -> 1.5
* Answer questions: r1, r4, r11, r13b, r14, r15

**DUE: Jan 26 before 10am**

**Solutions**

1. There is no difference. Throughout this text, the words “host” and “end system” are used interchangeably. End systems include PCs, workstations, Web servers, mail servers, PDAs, Internet-connected game consoles, etc.
4. 1. Dial-up modem over telephone line: home; 2. DSL over telephone line: home or small office; 3. Cable to HFC: home; 4. 100 Mbps switched Ethernet: enterprise; 5. Wifi (802.11): home and enterprise: 6. 3G and 4G: wide-area wireless.
11. At time t0 the sending host begins to transmit. At time t1 = L/R1, the sending host completes transmission and the entire packet is received at the router (no propagation delay). Because the router has the entire packet at time t1, it can begin to transmit the packet to the receiving host at time t1. At time t2 = t1 + L/R2, the router completes transmission and the entire packet is received at the receiving host (again, no propagation delay). Thus, the end-to-end delay is L/R1 + L/R2.
13. a) 2 users can be supported because each user requires half of the link bandwidth.

	b) Since each user requires 1Mbps when transmitting, if two or fewer users transmit simultaneously, a maximum of 2Mbps will be required. Since the available bandwidth of the shared link is 2Mbps, there will be no queuing delay before the link. Whereas, if three users transmit simultaneously, the bandwidth required will be 3Mbps which is more than the available bandwidth of the shared link. In this case, there will be queuing delay before the link.
	
	c) Probability that a given user is transmitting = 0.2 ⎛3⎞ 3 3−3 
	
	d) Probability that all three users are transmitting simultaneously = ⎜3⎟p (1− p) 3⎝⎠ = (0.2) = 0.008. Since the queue grows when all the users are transmitting, the fraction of time during which the queue grows (which is equal to the probability that all three users are transmitting simultaneously) is 0.008.

14. If the two ISPs do not peer with each other, then when they send traffic to each other they have to send the traffic through a provider ISP (intermediary), to which they have to pay for carrying the traffic. By peering with each other directly, the two ISPs can reduce their payments to their provider ISPs. An Internet Exchange Points (IXP) (typically in a standalone building with its own switches) is a meeting point where multiple ISPs can connect and/or peer together. An ISP earns its money by charging each of the the ISPs that connect to the IXP a relatively small fee, which may depend on the amount of traffic sent to or received from the IXP.

15. Google's private network connects together all its data centers, big and small. Traffic between the Google data centers passes over its private network rather than over the public Internet. Many of these data centers are located in, or close to, lower tier ISPs. Therefore, when Google delivers content to a user, it often can bypass higher tier ISPs. What motivates content providers to create these networks? First, the content provider has more control over the user experience, since it has to use few intermediary ISPs. Second, it can save money by sending less traffic into provider
networks. Third, if ISPs decide to charge more money to highly profitable content providers (in countries where net neutrality doesn't apply), the content providers can avoid these extra payments.


HW 02
---

----

Jan 26

* Finish reading sections 1.4 -> 1.6
* Answer questions (r16, r17, r20, r23, r24)

**DUE: Jan 28 before 10am**


R16. Consider sending a packet from a source host to a destination host over a fixed route. List the delay components in the end-to-end delay. Which of these delays are constant and which are variable?
R17. Visit the Transmission Versus Propagation Delay applet at the companion Web site. Among the rates, propagation delay, and packet sizes available, find a combination for which the sender finishes transmitting before the first bit of the packet reaches the receiver. Find another combination for which the first bit of the packet reaches the receiver before the sender finishes transmitting.


[http://wps.aw.com/aw_kurose_network_4/63/16303/4173752.cw/index.html](http://wps.aw.com/aw_kurose_network_4/63/16303/4173752.cw/index.html)

R20. Suppose end system A wants to send a large file to end system B. At a very high level, describe how end system A creates packets from the file. When one of these packets arrives to a packet switch, what information in the packet does the switch use to determine the link onto which the packet is forwarded? Why is packet switching in the Internet analogous to driving from one city to another and asking directions along the way?
R23. What are the five layers in the Internet protocol stack? What are the principal responsibilities of each of these layers?
R24. What is an application-layer message? A transport-layer segment? A network- layer datagram? A link-layer frame?

**Solutions**

16. The delay components are processing delays, transmission delays, propagation delays, and queuing delays. All of these delays are fixed, except for the queuing delays, which are variable.

17. a) 1000 km, 1 Mbps, 100 bytes b) 100 km, 1 Mbps, 100 bytes

20. End system A breaks the large file into chunks. It adds header to each chunk, thereby generating multiple packets from the file. The header in each packet includes the IP address of the destination (end system B). The packet switch uses the destination IP address in the packet to determine the outgoing link. Asking which road to take is analogous to a packet asking which outgoing link it should be forwarded on, given the packet’s destination address.

23. The five layers in the Internet protocol stack are – from top to bottom – the application layer, the transport layer, the network layer, the link layer, and the physical layer. The principal responsibilities are outlined in Section 1.5.1.
24. Application-layer message: data which an application wants to send and passed onto the transport layer; transport-layer segment: generated by the transport layer and encapsulates application-layer message with transport layer header; network-layer datagram: encapsulates transport-layer segment with a network-layer header; link- layer frame: encapsulates network-layer datagram with a link-layer header.



HW 03
---

----

Jan 28

* **Reading** Kurose & Ross - Chapter 2.1
* Answer questions (r2, r5, r6, r7, r8)

**DUE: Feb 02 before 10am**

R2. What is the difference between network architecture and application architecture?
R5. What information is used by a process running on one host to identify a process running on another host?
R6. Suppose you wanted to do a transaction from a remote client to a server as fast as possible. Would you use UDP or TCP? Why?
R7. Referring to Figure 2.4, we see that none of the applications listed in Figure 2.4 requires both no data loss and timing. Can you conceive of an application that requires no data loss and that is also highly time-sensitive?
R8. List the four broad classes of services that a transport protocol can provide. For each of the service classes, indicate if either UDP or TCP (or both) pro- vides such a service.

**Solutions**

2. Network architecture refers to the organization of the communication process into layers (e.g., the five-layer Internet architecture). Application architecture, on the other hand, is designed by an application developer and dictates the broad structure of the application (e.g., client-server or P2P).
5. The IP address of the destination host and the port number of the socket in the destination process.
6. You would use UDP. With UDP, the transaction can be completed in one roundtrip time (RTT) - the client sends the transaction request into a UDP socket, and the server sends the reply back to the client's UDP socket. With TCP, a minimum of two RTTs are needed - one to set-up the TCP connection, and another for the client to send the request, and for the server to send back the reply.
7. One such example is remote word processing, for example, with Google docs. However, because Google docs runs over the Internet (using TCP), timing guarantees are not provided.
8. 
a) Reliable data transfer
TCP provides a reliable byte-stream between client and server but UDP does not.

b) A guarantee that a certain value for throughput will be maintained Neither

c) A guarantee that data will be delivered within a specified amount of time Neither

d) Confidentiality (via encryption) Neither


HW 04
---

----

Feb 02

**DUE: Feb 05 before 5pm**

**Reading** [https://docs.python.org/2/library/socket.html](https://docs.python.org/2/library/socket.html)

**Source code** [server.py](/457/hw/server/) [client.py](/457/hw/client/)

Write a simple client server application using python socket (networking) api. The client server application should simulate something like the HTTP protocol. 

The server side of the application maintains a list of "data" keyed by an index. You can use this:

	server_data = {'oranges': 'yummy', 'grapes': 'wine is fine', 'apples': 'too tart', 'peaches': 'just peachee!', 'plums': 'great but no prunes'}

To access a value by key:
	
	server_data['plums']  # should return 'great but no prunes'

Our *application protocol* is:

1. Send request containing a key (e.g., oranges).
2. If server finds value associated with key:
	- Send message containing value to client.
3. Else
	- Send message about key not found to client.
4. Client displays the message from server.


REQUEST MESAGE FORMAT ==> simply send a key


Example Client sends message:

	'oranges'

Example Server sends response:

	'yummy'

Example Client sends message:

	'bananas'

Example Server sends response:

	'Resource not found.'


HW 05
---

----

Feb 04

**DUE: Feb 10 before 5pm** [Submit to D2L](https://nmhu.desire2learn.com/d2l/home/28405)

**Reading** 


[python BaseHTTPServer (you need this to utilize existing code for a server)](https://docs.python.org/2/library/basehttpserver.html)

[python HTTPRequestHandler (you need this handle http request from client)](https://docs.python.org/2/library/basehttpserver.html#BaseHTTPServer.BaseHTTPRequestHandler)


**Source code** [fruit-basket.py](/457/hw/fruit-basket/) [fruit-chooser.html](/457/hw/fruit-chooser/)

Write another client/server application. This time you will implement ```HTTP 1.1``` on the server side and use a regular ol' browser for the client. To implement the server you will use the **SimpleHttpServer** python module (examples of how to use this are linked above). Your simple http server will perform the same function as the one specified in [HW 4](#hw-04), that is, it will receive a *key* from the client, do a look up of the key in a dictionary (known to the server of course) and return the associated value to the client. You can use the same fruit dictionary used in hw 4 or make up your own. The point is that you get experience handling an HTTP request as delivered by a modern web browser such as Google Chrome or others (the client). Further specifications:

> the browser (client) will send a requested **key** input via a form in a simple html page. The form will send the key with the ```GET``` command (or method as the form knows it). The resulting key request will be attached to the url to your server - also known as a **query parameter**. You can use the example html file above if you like but you need to provide the correct METHOD and ACTION. What are these for? 

**Solution: fruit-basket-server.py**

{% highlight python %}
	#!/usr/bin/python
	from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

	from urlparse import urlparse, parse_qs

	PORT_NUMBER = 8080

	#This class will handle any incoming request from the browser 
	class myHandler(BaseHTTPRequestHandler):
		fruit_basket = {'oranges': 'yummy', 'grapes': 'wine is fine', 'apples': 'too tart', 'peaches': 'just peachee!', 'plums': 'great but no prunes'}
		
		#Handler for the GET requests
		def do_GET(self):

			fruit_query = parse_qs(urlparse(self.path).query)
			f = fruit_query["fruitykey"] # Matches 'name' attribute in form
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			# Send the html message
			try:
				self.wfile.write(self.fruit_basket[f[0]])
			
			except Exception as e:
				self.wfile.write('Resource not found')
			
			return

	try:
		#Create a web server and define the handler to manage the
		#incoming request
		server = HTTPServer(('', PORT_NUMBER), myHandler)
		print 'Started httpserver on port ' , PORT_NUMBER
		
		#Wait forever for incoming htto requests
		server.serve_forever()

	except KeyboardInterrupt:
		print '^C received, shutting down the web server'
		server.socket.close()
{% endhighlight %}

HW 06
---

Feb 11

**Reading:** Kurose & Ross - 2.7

**Source code** [download udp-pinger-server.py]({{ site.baseurl }}assets/udp-pinger-server.py) and see below for more details on the client specification (the part you are writing)

**DUE: Feb 17 before 5pm** [Submit only your ```client``` source code to D2L HW06 dropbox](https://nmhu.desire2learn.com/d2l/home/28405){:target="_blank"}


**How to handle time in python?**

> 	import time
> 	t1 = time.time()  # yields current time.
> 	t2 = time.time()  # yields current time.
> 	# you can find the delta between two times simply by taking t2-t1

**How to set a timeout on a socket (i.e., make the socket throw an exception when/if the timeout is exceeded)?**

[read about setting a timeout on a socket](https://docs.python.org/2/library/socket.html#socket.socket.settimeout){:target="_blank"}

**Note that the ```settimeout``` method throws an exception. So your code for receiving a response from the UDP server needs to be in a try / exception block like this:**


>	try:
>		# something in here may throw an exception
>		...
>		# there may be many statements in here!
>
>	except:
>		# what do to in case of exception
>		...
>


**Specification** Assignment 2: UDP Pinger (from textbook pg 179)

In this programming assignment, you will write a client ping program in Python. Your client will send a simple ping message to a server, receive a corresponding pong message back from the server, and determine the delay between when the client sent the ping message and received the pong message. This delay is called the Round Trip Time (RTT). The functionality provided by the client and server is
similar to the functionality provided by standard ping program available in modern operating systems. However, standard ping programs use the Internet Control Message Protocol (ICMP) (which we will study in Chapter 4). Here we will create a nonstandard (but simple!) UDP-based ping program.

Your ping program is to send 10 ping messages to the target server over UDP. For each message, your client is to determine and print the RTT when the corresponding pong message is returned. Because UDP is an unreliable protocol, a packet sent by the client or server may be lost. For this reason, the client cannot wait indefinitely for a reply to a ping message. You should have the client wait up to one second for a reply from the server; if no reply is received, the client should assume that the packet was lost and print a message accordingly.
In this assignment, you will be given the complete code for the server (available in the companion Web site). Your job is to write the client code, which will be very similar to the server code. It is recommended that you first study carefully the server code. You can then write your client code, liberally cutting and pasting lines from the server code.

The [```udp-pinger-server.py```]({{ site.baseurl }}assets/udp-pinger-server.py) code fully implements a ping server. You need to compile and run this code before running your client program. You do not need to modify this code. In this server code, 30% of the client’s packets are simulated to be **lost**. You should study this code carefully, as it will help you write your ping client. 


**Client Code (more info)** 

You need to implement the following client program. The client should send 10 pings to the server. Because UDP is an unreliable protocol, a packet sent from the client to the server may be lost in the network, or vice versa. For this reason, the client cannot wait indefinitely for a reply to a ping message. You should get the client to wait up to one second for a reply; if no reply is received within one second, your client program should assume that the packet was lost during transmission across the network. You will need to look up the Python documentation to find out how to set the timeout value on a datagram socket. Specifically, your client program should 

(1) send the ping message using UDP (Note: Unlike TCP, you do not need to establish a connection first, since UDP is a connectionless protocol.)

(2) print the response message from server, if any 

(3) calculate and print the round trip time (RTT), in seconds, of each packet, if server responses 

(4) otherwise, print “Request timed out” 

During development, you should run the [```udp-pinger-server.py```]({{ site.baseurl }}assets/udp-pinger-server.py) on your machine, and test your client by sending packets to localhost (or, 127.0.0.1). After you have fully debugged your code, you should see how your application communicates across the network with the ping server and ping client running on different machines. 

**Message Format (what to send to server):** 

Ping ```sequence number``` ```time```

Ping ```sequence number``` where sequence number starts at 1 and progresses to 10 for each successive ping message sent by the client, and ```time``` is the time when the client sends the message (use ```time.asctime()```).

**Example message to send to ```udp-pinger-server```:**

>	Ping 1 Thu Feb 11 12:54:55 2016


**Example output from running the client:**

>	Request timed out.
>	Reply from 127.0.0.1: PING 2 THU FEB 11 12:54:56 2016
>	RTT: 0.0010359287262
>	Reply from 127.0.0.1: PING 3 THU FEB 11 12:54:56 2016
>	RTT: 0.000565052032471
>	Reply from 127.0.0.1: PING 4 THU FEB 11 12:54:56 2016
>	RTT: 0.000596046447754
>	Request timed out.
>	Request timed out.
>	Request timed out.
>	Request timed out.
>	Reply from 127.0.0.1: PING 9 THU FEB 11 12:55:00 2016
>	RTT: 0.00111699104309
>	Reply from 127.0.0.1: PING 10 THU FEB 11 12:55:00 2016
>	RTT: 0.000634908676147

**Solution: udp-pinger-client.py**

{% highlight python %}
	import time
	from socket import *

	host = 'localhost'
	port = 12000
	timeout = 1 # in seconds
	 
	# Create UDP client socket
	# Note the use of SOCK_DGRAM for UDP datagram packet
	clientsocket = socket(AF_INET, SOCK_DGRAM)
	# Set socket timeout as 1 second
	clientsocket.settimeout(timeout)
	# Command line argument is a string, change the port into integer
	port = int(port)  
	# Sequence number of the ping message
	ptime = 0  

	# Ping for 10 times
	while ptime < 10: 
	    ptime += 1
	    # Format the message to be sent
	    data = "Ping " + str(ptime) + " " + time.asctime()
	    
	    try:
		# Sent time
	        RTTb = time.time()
		# Send the UDP packet with the ping message
	        clientsocket.sendto(data,(host, port))
		# Receive the server response
	        message, address = clientsocket.recvfrom(1024)  
		# Received time
	        RTTa = time.time()
		# Display the server response as an output
	        print "Reply from " + address[0] + ": " + message       
		# Round trip time is the difference between sent and received time
	        print "RTT: " + str(RTTa - RTTb)
	    except:
	        # Server does not respond
	        # Assume the packet is lost
	        print "Request timed out."
	        continue

	# Close the client socket
	clientsocket.close()

{% endhighlight %}

HW 07 
---

Python programming exercises

Feb 16

**Reading:**
[[python list tutorial]](https://docs.python.org/2/tutorial/datastructures.html),
[[python dictionary docs]](https://docs.python.org/2/library/stdtypes.html#mapping-types-dict),
[[dictionary tutorial]](http://learnpythonthehardway.org/book/ex39.html),
[[python pickle]](https://docs.python.org/3/library/pickle.html), 
[[python json]](https://docs.python.org/3/library/json.html)

**DUE: Feb 18 before 5pm** [Submit your source code file to HW07 dropbox](https://nmhu.desire2learn.com/d2l/home/28405){:target="_blank"}

**Specification**: Python programming exercises

Create one python source file for the following exercises:

[0] Use the ```range``` function to generate and store a LIST of values (0 through 10) in a variable named ```primero```. Then loop through the list updating each value by squaring it. Print ```primero``` to the console verifying that the values were updated.

[1] Create a list (c/p the following.)

>	raw_data = ['Roses', 'are', 'red', 'violets', 'are', 'blue', 'if', 'you', 'can', 'read', 'this', 'so', 'are', 'you.']

[2] Print the length of ```raw_data```.

[3] Print the index of the word ```violets``` then print the index of ```you``` (*which* index was returned?). 

[4] Loop through ```raw_data```, printing each of its items on a line.

[5] Create an empty dictionary e.g., ```db = {}``` then populate it with data from ```raw_data```. Use an index for the key. For example, the first two key value pairs would look like ==> ```{0 : 'Roses', 1 : 'are', ...}```. **HINT: use ```range``` to loop ```len(raw_data)``` times.** After building the dictionary, loop through it printing each key and value together on a line.

>	for key, value in somedictionary:
>		# do something with the key
>		# do something with the value

[6] **lookups**: With the dictionary created in ex 5, query for the following values ==> 0, 6, 20 printing the result of each query. Make sure you handle ```KeyErrors``` e.g,

>	try:
>		dictionary lookup
>	except KeyError:
>		'Not found!'

[7] **serialization**: First, ```import json``` then serialize the dictionary created in ex 5 using ```json.dumps``` (Store the output to variable ```jsonified```). Note the transformation of the key and note that ```json.loads(jsonified)``` gives you a new dictionary ... for free!

[8] **deserialization** deserialize ```jsonified``` using ```json.loads```. Note the transformation of the key. Is it still an ```int```?

[9] Now repeat steps [7] and [8] this time using ```pickle.dumps``` (store output in variable ```pickonme```) and ```pickle.loads``` (```import pickle``` first!). Note the output of both steps. Does ```pickle``` preserve the data type of the key and the value?

[10] 1. Create an empty dictionary named ```deserious```. Create another variable ```source``` that stores the output of ```json.loads(jsonified)```. ```source``` should be a dictionary. Loop through the ```source``` dictionary, each time **coercing** the ```key``` to an integer and adding the new integer key to the ```deserious``` dictionary along with the value.  Your are essentially building a new dictionary with ```int``` keys rather than string keys.

One can loop through a dictionary (reading each KEY and VALUE) again like this:

>	for key, value in somedictionary:
>		# do something with the key
>		# do something with the value


HW 08 
---

cs457p2p application: Part 1

Feb 23

**Reading:**
[[python list tutorial]](https://docs.python.org/2/tutorial/datastructures.html),
[[python dictionary docs]](https://docs.python.org/2/library/stdtypes.html#mapping-types-dict),
[[dictionary tutorial]](http://learnpythonthehardway.org/book/ex39.html),
[[python pickle]](https://docs.python.org/3/library/pickle.html), 
[[python json]](https://docs.python.org/3/library/json.html)

**Code**: [download tracker-p1.py](/assets/tracker-p1.py) this code is also displayed below.

**READ!!!! the protocol ==>**[protocol part 1](/457/hw/cs457p2p-protocol-part1/)

**DUE: Feb 25 before 5pm** [Submit your source code file to HW08 dropbox](https://nmhu.desire2learn.com/d2l/home/28405){:target="_blank"}

**Specification**: A peer-to-peer client

You are going to write a simple p2p client that connects to central server in order to collect db items. The client must follow the protocol listed [here](/457/hw/cs457p2p-protocol-part1/) to successfully participate in this network application. The client's work is done when it has assembled all of the db items. It must print the db items in their logical order before exiting.

The protocol lays out the sequence of steps needed to register and then request db items. Your client will need to connect to a TRACKER server. That code is listed above and you can use it without modification to test your client code. 

1. The client should use the TCP protocol (not UDP)
2. The client should pause (use timer) for 2-3 seconds between db item requests. This simulates network lag.
3. All db item requests MUST be ```serialized``` before sending to ```TRACKER```. Use pickle for this.

Below is pseudocode to help you get started:

>	1. connect to TRACKER to request REGISTRATION
> 
>	2. deserialize TRACKER's response and store in variable N where N is the size of the db.
> 
>	3. create an empty dict to store the db items as you collect them
> 
>	4. loop 0 -> N-1 times, each time making connection to TRACKER and requesting an item indicated by the loop's iteration seq. All requests must be serialized before sending to TRACKER
> 
>		4a. process each response from the TRACKER by deserializing the packet and storing in local dict created above. Note that the packet contains a seq number and a value. Use the seq number as a key into the dict and associated it with the value.
> 
>	5. after loop ends, reassemble the db items stored in local dict to print the db in logical order.
> 
> 	6. You should see an important message for the next phase of this p2p application


**tracker-p1.py** [download tracker-p1.py](/assets/tracker-p1.py)

{% highlight python %}
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

{% endhighlight %}

**starter client file**

{% highlight python %}

	#!/usr/bin/env python

	"""Simple p2p client starter file for cs457p2p application PART 1"""

	import socket
	import pickle
	import time

	#  server host (local machine)
	host = 'localhost' 

	#  machine port
	port = 7777

	#  number of requests before need to thread...
	backlog = 5

	#  max length of data buffer (bytes) 
	size = 1024


	#  create a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.connect((host, port))

	# SEND/PROCESS  REGISTRATION REQUEST

	# SEND/PROCESS ITEM REQUESTS

{% endhighlight %}
	

HW 09
---

cs457p2p application: Part 2

**Solution:**

{% highlight python %}
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
{% endhighlight %}

Mar 3

**Reading:**
[[python pickle]](https://docs.python.org/3/library/pickle.html)


**Code**: 

[download p2p-tracker.py](/assets/p2p-tracker.py) 

[download p2p-threaded-client-server-starter.py](/assets/p2p-threaded-client-server-starter.py) 


**READ!!!! the protocol ==>**[protocol part 2](/457/hw/cs457p2p-protocol-part2/)

**DUE: Mar 14 before 5pm** [Submit your source code file to HW09 dropbox](https://nmhu.desire2learn.com/d2l/home/28405){:target="_blank"}

**Specification**: A peer-to-peer client

You are going to write a simple p2p client that connects to other peers to collect db items. The client must follow the protocol listed [here](/457/hw/cs457p2p-protocol-part2/) to successfully participate in this network application. The client's work is done when it has assembled all of the db items. It must print the db items in their logical order before exiting. The server must remain running to provide services to other peers.

The protocol lays out the sequence of steps needed to register and then request db items. Your client will need to connect to a TRACKER server. That code is listed above and you can use it without modification to test your client code. 

1. The client should use the TCP protocol (not UDP)
2. The client should pause (use timer) for 2-3 seconds between db item requests. This simulates network lag.
3. All db item requests MUST be ```serialized``` before sending to ```NEIGHBOR_CONNECTION```. Use pickle for this.

Below is pseudocode to help you get started:

>	1. connect to TRACKER to request REGISTRATION


NOTE: In the starter file, you need to send your port number in REGISTRATION request. It may not be clear but you can use: 
----


>	message = ('REGISTER', MYHANDLE, MYSERVER_CONNECTION[1])



>	2. deserialize TRACKER's response and store neighbor's handle, ip address, and port number as a tuple in NEIGHBOR_CONNECTION. Also initialize DB_LEN and the add the db item the tracker sent to your DB (see next step).
> 
>	3. your local db is a dictionary named DB. Add the db item sent to you by the tracker during REGISTRATION to this dictionary. It is your seed item.
> 
>	4. loop until you have collected all items from NEIGHBOR_CONNECTION. Each iteration should make a connection to NEIGHBOR_CONNECTION requesting an item indicated by the first item you do not have. All requests must be serialized before sending to NEIGHBOR_CONNECTION. See QUERY request format in protocol.
> 
>		4a. Each QUERY request should get a response. Unpack this response accordingly. If it has data (e.g. not None) then you can place the item in your DB, else keep querying the neighbor for the item. If you get a successful response, begin querying the next item you don't have. HINT: Inspect function get_next_item() to help determine which you need next.
> 
>	5. after loop ends, reassemble the db items stored in local dict to print the db in logical order.
> 
> 	6. You should see a complete, grammatically correct message.


**Specification**: A peer-to-peer server

1. The server thread should handle requests as follows:

>	QUERY -- should unpack query message and lookup requested item in DB. If the item is found, the server should send using response format QUERY_RESULT. If the item is not found in DB, then return (None, None) as a database item.

>	PING  (message from Tracker) -- should unpack PING requests and simply return ('ACK', MYHANDLE)

>	UPDATE_NBR (message from Tracker) -- should unpack request and overwrite NEIGHBOR_CONNECTION with the tuple sent by the TRACKER.


HW 10
---

Answer the following questions from Chapter 3 of the textbook. Submit responses in a text file to D2L.

**DUE Apr 1 at 5pm**

Questions (please note that the questions listed in the text are grouped by section number. This should help you locate the appropriate info.) ==> 

```R3, R4, R6, R12, R13, R14, R15, R18```

**See this to access applets** ==> [http://wps.aw.com/aw_kurose_network_4/63/16303/4173752.cw/index.html](http://wps.aw.com/aw_kurose_network_4/63/16303/4173752.cw/index.html)

**Solution**

R3. Consider a TCP connection between Host A and Host B. Suppose that the TCP segments traveling from Host A to Host B have source port number x and destination port number y. What are the source and destination port numbers for the segments traveling from Host B to Host A?

**Source port number y and destination port number x.**

R4. Describe why an application developer might choose to run an application over UDP rather than TCP.

**An application developer may not want its application to use TCP’s congestion control, which can throttle the application’s sending rate at times of congestion. Often, designers of IP telephony and IP videoconference applications choose to run their applications over UDP because they want to avoid TCP’s congestion control. Also, some applications do not need the reliable data transfer provided by TCP.**

R6. Is it possible for an application to enjoy reliable data transfer even when the application runs over UDP? If so, how?

**Yes. The application developer can put reliable data transfer into the application layer protocol. This would require a significant amount of work and debugging, however.**

R12. Visit the Go-Back-N Java applet at the companion Web site.
a. Have the source send five packets, and then pause the animation before any of the five packets reach the destination. Then kill the first packet and resume the animation. Describe what happens.

b. Repeat the experiment,but now let the first packet reach the destination and kill the first acknowledgment. Describe again what happens.

c. Finally,try sending six packets. What happens?

	a) The packet loss caused a time out after which all the five packets were retransmitted.
	b) Loss of an ACK didn’t trigger any retransmission as Go-Back-N uses cumulative acknowledgements.
	c) The sender was unable to send sixth packet as the send window size is fixed to 5.

R13. Repeat R12, but now with the Selective Repeat Java applet. How are Selective Repeat and Go-Back-N different?

	a) When the packet was lost, the received four packets were buffered the receiver. After
	the timeout, sender retransmitted the lost packet and receiver delivered the buffered packets to application in correct order.
	b) Duplicate ACK was sent by the receiver for the lost ACK.
	c) The sender was unable to send sixth packet as the send window size is fixed to 5
	When a packet was lost, GO-Back-N retransmitted all the packets whereas Selective Repeat retransmitted the lost packet only. In case of lost acknowledgement, selective repeat sent a duplicate ACK and as GO-Back-N used cumulative acknowledgment, so that duplicate ACK was unnecessary.

R15. Suppose Host A sends two TCP segments back to back to Host B over a TCP connection. The first segment has sequence number 90; the second has sequence number 110.
a. Howmuchdataisinthefirstsegment?
b. SupposethatthefirstsegmentislostbutthesecondsegmentarrivesatB. In the acknowledgment that Host B sends to Host A, what will be the acknowledgment number?

**a) 20 bytes b) ack number = 90**

R18. True or false? Consider congestion control in TCP. When the timer expires at the sender, the value of ssthresh is set to one half of its previous value.

**False, it is set to half of the current value of the congestion window.**


HW 11
---

This assignment has two parts:

a) Answer questions ```R2, R3, R9, R17``` from Chapter 4 of the text.

b) Answer questions ```1-9``` from the wireshark lab. Submit responses in a text file to D2L.

The wireshark lab sheet is here ==> [wireshark-lab-ip.pdf](/assets/wireshark-lab-ip.pdf)

**DUE Apr 8 at 5pm**

**Solutions**

R2. What are the two most important network-layer functions in a datagram net- work? What are the three most important network-layer functions in a virtual- circuit network?

**Datagram-based network layer: forwarding; routing. Additional function of VC-based network layer: call setup.**

R3. What is the difference between routing and forwarding?

**Forwarding is about moving a packet from a router’s input port to the appropriate output port. Routing is about determining the end-to-routes between sources and destinations.**

R9. Describe how packet loss can occur at input ports. Describe how packet loss at input ports can be eliminated (without using infinite buffers).

**If the rate at which packets arrive to the fabric exceeds switching fabric rate, then packets will need to queue at the input ports. If this rate mismatch persists, the queues will get larger and larger and eventually overflow the input port buffers, causing packet loss. Packet loss can be eliminated if the switching fabric speed is at least n times as fast as the input line speed, where n is the number of input ports.**

R17. Suppose Host A sends Host B a TCP segment encapsulated in an IP datagram. When Host B receives the datagram, how does the network layer in Host B know it should pass the segment (that is, the payload of the datagram) to TCP rather than to UDP or to something else?

**The 8-bit protocol field in the IP datagram contains information about which transport layer protocol the destination host should pass the segment to.**


HW 12
---

Answer questions ```R19, R20, R21, R22``` and ```P1 and P26``` from Chapter 4 of the text.

The following animated slides may help with P26:

[dijkstra-shortest-path-demo.pptx](/assets/dijkstra-shortest-path-demo.pptx)

[dijkstra-shortest-path-demo-2.pptx](/assets/dijkstra-shortest-path-demo-2.pptx)

**DUE Apr 18 at 5pm**

**Solutions**

R19. Compare and contrast the IPv4 and the IPv6 header fields. Do they have any fields in common?

**IPv6 has a fixed length header, which does not include most of the options an IPv4 header can include. Even though the IPv6 header contains two 128 bit addresses (source and destination IP address) the whole header has a fixed length of 40 bytes only. Several of the fields are similar in spirit. Traffic class, payload length, next header and hop limit in IPv6 are respectively similar to type of service, datagram
length, upper-layer protocol and time to live in IPv4.**

R20. It has been said that when IPv6 tunnels through IPv4 routers, IPv6 treats the IPv4 tunnels as link-layer protocols. Do you agree with this statement? Why or why not?

**Yes, because the entire IPv6 datagram (including header fields) is encapsulated in an IPv4 datagram.**

R21. Compare and contrast link-state and distance-vector routing algorithms.

**Link state algorithms: Computes the least-cost path between source and destination using complete, global knowledge about the network. Distance-vector routing: The calculation of the least-cost path is carried out in an iterative, distributed manner. A node only knows the neighbor to which it should forward a packet in order to reach given destination along the least-cost path, and the cost of that path from itself to the destination.**

R22. Discuss how a hierarchical organization of the Internet has made it possible to scale to millions of users.

**Routers are organized into autonomous systems (ASs). Within an AS, all routers run the same intra-AS routing protocol. The problem of scale is solved since an router in an AS need only know about routers within its AS and the subnets that attach to the AS. To route across ASes, the inter-AS protocol is based on the AS graph and does not take individual routers into account.**

P1. In this question, we consider some of the pros and cons of virtual-circuit and datagram networks.

a. Supposethatroutersweresubjectedtoconditionsthatmightcausethem to fail fairly often. Would this argue in favor of a VC or datagram archi- tecture? Why?

b. Supposethatasourcenodeandadestinationrequirethatafixedamount of capacity always be available at all routers on the path between the source and destination node, for the exclusive use of traffic flowing between this source and destination node. Would this argue in favor of a VC or datagram architecture? Why?

c. Supposethatthelinksandroutersinthenetworkneverfailandthatrout- ing paths used between all source/destination pairs remains constant. In this scenario, does a VC or datagram architecture have more control traf- fic overhead? Why?

	a) With a connection-oriented network, every router failure will involve the routing of that connection. At a minimum, this will require the router that is “upstream” from the failed router to establish a new downstream part of the path to the destination node, with all of the requisite signaling involved in setting up a path. Moreover, all of the routers on the initial path that are downstream from the failed node must take down the failed connection, with all of the requisite signaling involved to do this.

	With a connectionless datagram network, no signaling is required to either set up a new downstream path or take down the old downstream path. We have seen, however, that routing tables will need to be updated (e.g., either via a distance vector algorithm or a link state algorithm) to take the failed router into account. We have seen that with distance vector algorithms, this routing table change can sometimes be localized to the area near the failed router. Thus, a datagram network would be preferable. Interestingly, the design criteria that the initial ARPAnet be able to function under stressful conditions was one of the reasons that datagram architecture was chosen for this Internet ancestor.

	b) In order for a router to maintain an available fixed amount of capacity on the path between the source and destination node for that source-destination pair, it would need to know the characteristics of the traffic from all sessions passing through that link. That is, the router must have per-session state in the router. This is possible in a connection-oriented network, but not with a connectionless network. Thus, a connection-oriented VC network would be preferable.

	c) In this scenario, datagram architecture has more control traffic overhead. This is due to the various packet headers needed to route the datagrams through the network. But in VC architecture, once all circuits are set up, they will never change. Thus, the signaling overhead is negligible over the long run.

P26. Consider the following network. With the indicated link costs, use Dijkstra’s shortest-path algorithm to compute the shortest path from x to all network nodes. Show how the algorithm works by computing a table similar to Table 4.3.

![see graph](/assets/images/link-state-p26-graph.png)

![see table solution](/assets/images/link-state-p26-table-sol.png)

hw 13
---
Answer questions ```R1, R5, R9, R11``` from Chapter 5 of the text.

**DUE Apr 28 at 11am**

**Solutions**

R1. Consider the transportation analogy in Section 5.1.1. If the passenger is analagous to a datagram, what is analogous to the link layer frame?

**The transportation mode, e.g., car, bus, train, car.**

R5. In Section 5.3, we listed four desirable characteristics of a broadcast channel. Which of these characteristics does slotted ALOHA have? Which of these characteristics does token passing have?

**Slotted Aloha: 1, 2 and 4 (slotted ALOHA is only partially decentralized, since it requires the clocks in all nodes to be synchronized). Token ring: 1, 2, 3, 4.**

R9. How big is the MAC address space? The IPv4 address space? The IPv6 address space?

**248 MAC addresses; 232 IPv4 addresses; 2128 IPv6 addresses.**

R11. Why is an ARP query sent within a broadcast frame? Why is an ARP response sent within a frame with a specific destination MAC address?

**An ARP query is sent in a broadcast frame because the querying host does not which adapter address corresponds to the IP address in question. For the response, the sending node knows the adapter address to which the response should be sent, so there is no need to send a broadcast frame (which would have to be processed by all the other nodes on the LAN).**

hw 14
---
**DUE May 2 at 11am**

a) Answer questions ```R1, R2, R5, R6, R7, R8``` from Chapter 6 of the text.

**Solutions**

R1. What does it mean for a wireless network to be operating in “infrastructure mode?” If the network is not in infrastructure mode, what mode of operation is it in, and what is the difference between that mode of operation and infra- structure mode?

**In infrastructure mode of operation, each wireless host is connected to the larger network via a base station (access point). If not operating in infrastructure mode, a network operates in ad-hoc mode. In ad-hoc mode, wireless hosts have no infrastructure with which to connect. In the absence of such infrastructure, the hosts themselves must provide for services such as routing, address assignment, DNS-like name translation, and more.**


R2. What are the four types of wireless networks identified in our taxonomy in Section 6.1? Which of these types of wireless networks have you used?

**a) Single hop, infrastructure-based b) Single hop, infrastructure-less c) Multi-hop, infrastructure-based d) Multi-hop, infrastructure-less**

R5. Describe the role of the beacon frames in 802.11.

**APs transmit beacon frames. An AP’s beacon frames will be transmitted over one of the 11 channels. The beacon frames permit nearby wireless stations to discover and identify the AP.**


R6. True or false: Before an 802.11 station transmits a data frame, it must first send an RTS frame and receive a corresponding CTS frame.

**False**

R7. Why are acknowledgments used in 802.11 but not in wired Ethernet?

**APs transmit beacon frames. An AP’s beacon frames will be transmitted over one of the 11 channels. The beacon frames permit nearby wireless stations to discover and identify the AP.**

R8. True or false: Ethernet and 802.11 use the same frame structure.

**False**


b) Write a short python script containing two functions --```encipher(cleartext)``` and ```decipher(ciphertext)```.

A simple substitution cipher is one that uses a specific mechanism to replace cleartext characters with other characters following a substitution algorithm. The simplest is to use a rotating offset. For example, using an offset of 10, one could substitute all letter a's in the cleartext with the letter k (k is the character at offset 10 from a). For the ```encipher``` function, build and return the cipher for the cleartext argument. The ```decipher``` does the reverse -- accepts a cipher as an argument and returns the original cleartext. Your python program should call your two functions in the logical order printing both the cipher and the deciphered text to verify success.

Your cipher should handle a subset of ascii characters (32-127) for a total of 95 characters.

**Hints**

You can use the following to generate your alphabet for the cipher. Remember the offset needs to rotate!

>	cipher_alphabet = [chr(i) for i in range(32, 127)]

>	you may find chr() and ord() useful for mapping between ascii and ordinal values.

I will test your program with the following cleartext:

>	blue skies and sn0wee peaks ~ means no surfing today.

**Solution**




