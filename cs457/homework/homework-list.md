---
layout: page
title: 
permalink: /457/hw/
---

> [hw-05 due feb 10](#hw-05)

> [hw-04 due feb 05](#hw-04)

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

**DUE: Feb 10 before 5pm**

**Reading** 


[python BaseHTTPServer (you need this to utilize existing code for a server)](https://docs.python.org/2/library/basehttpserver.html)

[python HTTPRequestHandler (you need this handle http request from client)](https://docs.python.org/2/library/basehttpserver.html#BaseHTTPServer.BaseHTTPRequestHandler)


**Source code** [fruit-basket.py](/457/hw/fruit-basket/) [fruit-chooser.html](/457/hw/fruit-chooser/)

Write another client/server application. This time you will implement ```HTTP 1.1``` on the server side and use a regular ol' browser for the client. To implement the server you will use the **SimpleHttpServer** python module (examples of how to use this are linked above). Your simple http server will perform the same function as the one specified in [HW 4](#hw-04), that is, it will receive a *key* from the client, do a look up of the key in a dictionary (known to the server of course) and return the associated value to the client. You can use the same fruit dictionary used in hw 4 or make up your own. The point is that you get experience handling an HTTP request as delivered by a modern web browser such as Google Chrome or others (the client). Further specifications:

> the browser (client) will send a requested **key** input via a form in a simple html page. The form will send the key with the ```GET``` command (or method as the form knows it). The resulting key request will be attached to the url to your server - also known as a **query parameter**. You can use the example html file above if you like but you need to provide the correct METHOD and ACTION. What are these for? 






