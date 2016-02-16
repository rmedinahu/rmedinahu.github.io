---
layout: page
title: 
permalink: /457/hw/
---

> [hw-07 due feb 18 @ 5pm](#hw-07)

> [hw-06 due feb 17 @ 5pm](#hw-06)

> [hw-05 due feb 10](#hw-05)

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


HW 07 
---

Python programming exercises

Feb 16

**Reading:**
[python list tutorial](https://docs.python.org/2/tutorial/datastructures.html),
[python dictionary docs](https://docs.python.org/2/library/stdtypes.html#mapping-types-dict),
[dictionary tutorial](http://learnpythonthehardway.org/book/ex39.html,)
[python pickle](https://docs.python.org/3/library/pickle.html), 
[python json](https://docs.python.org/3/library/json.html)

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

[7] **serialization**: First, ```import json``` then serialize the dictionary created in ex 5 using ```json.dumps``` (Store the output to variable ```jsonified```). Note the transformation of the key and note that ```loads``` gives you a new dictionary ... for free!

[8] **deserialization** deserialize ```jsonified``` using ```json.loads```. Note the transformation of the key. Is it still an ```int```?

[9] Now repeat steps [7] and [8] this time using ```pickle.dumps``` (store output in variable ```pickonme```) and ```pickle.loads``` (```import pickle``` first!). Note the output of both steps. Does ```pickle``` preserve the data type of the key and the value?

[10] 1. Create an empty dictionary named ```deserious```. Create another variable ```source``` that stores the output of ```json.loads(jsonified)```. ```source``` should be a dictionary. Loop through the ```source``` dictionary, each time **coercing** the ```key``` to an integer and adding the new integer key to the ```deserious``` dictionary along with the value.  Your are essentially building a new dictionary with ```int``` keys rather than string keys.

One can loop through a dictionary (reading each KEY and VALUE) again like this:

>	for key, value in somedictionary:
>		# do something with the key
>		# do something with the value





