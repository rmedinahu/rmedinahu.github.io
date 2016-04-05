---
layout: course_page
title: schedule
permalink: /457/schedule/
parent_course: 457
---

cs 457 *schedule of topics*
------

Jump to week[n] ==> [12](#week-12), [11](#week-11), [10](#week-10), [8](#week-8), [7](#week-7), [6](#week-6), [5](#week-5), [4](#week-4), [3](#week-3), [2](#week-2), [1](#week-1)


---


Week 1
------

Jan 19 *introduction*
------

Jan 21 *overview internet architecture*
------
**chapter** 1, **slides**: Chapter_1_V6.1.ppt

- network edge
- communication link types
- 'last mile' technology
- access isp's
- HW01 assigned


---

Week 2
------

Jan 26 *overview internet architecture*
------
**chapter** 1, **slides**: Chapter_1_V6.1.ppt

- network core
- packet switching - circuit switching
- delays (queue, nodal, transmission, propogation)
- store and forward
- queues
- HW02 assigned

Jan 28 *application layer overview*
------
**chapter** 1.5, 1.6, 2.1, **slides**: Chapter_1_V6.1.ppt, Chapter_2_V6.3.ppt

- demo traceroute - illustrate delay
- internet protocol stack review (ch1)
- overview application layer
- network application software
- developer facing / network is abstraction
- client-server / p2p
- socket api (application prog interface)
- transport services: reliable, throughput, timing,security
- HW03 assigned


---


Week 3
------

Feb 02 *application layer protocols*
------
**chapter** 2.2, 2.3, **slides**: Chapter_2_V6.3.ppt

- application layer protocol
- web protocol: http, html
- [HW04 assigned](/457/hw/) - client/server application in python

Feb 04 *application layer protocols*
------
**chapter** 2.2, 2.3, **slides**: Chapter_2_V6.3.ppt

> Can you conceive of an application that requires no data loss and that is also highly time-sensitive?

No data loss AND time sensitive? Where would we need this?

stock market ticker, breaking a car remotely over the network, remote surgery, security alarms, no such application exists, remote rescue, navigating museum, UAV control, drone aircraft, multiplayer video game app that forces you to attack each other with words, search and rescue drone

- Basic client server application review
- Simple web server for handling fruit
- [HW05 assigned](/457/hw/) - client/server web application in python


---


Week 4
------

Feb 09 *application layer protocols continued*
------
**chapter** 2.3, 2.4, 2.5, 2.7 **slides**: Chapter_2_V6.3.ppt

**files**: [wireshark-lab-intro.pdf]({{ site.baseurl }}assets/wireshark-lab-intro.pdf)

- FTP, SMTP Application layer protocol
- DNS overview (as application)
- complete wireshark introductory lab at home before next class

Feb 11 *socket and application programming*
------
**chapter** 2.6, 2.7 **slides**: Chapter_2_V6.3.ppt

- peer to peer apps ( BitTorrent, DHA)
- socket programming
- UDP client-server
- [HW06 assigned](/457/hw/) - client/server UDP ping program



---


Week 5
------

Feb 16 *socket and application programming*
------
**chapter** 2.7

**online** 
[python list tutorial](https://docs.python.org/2/tutorial/datastructures.html),
[python dictionary docs](https://docs.python.org/2/library/stdtypes.html#mapping-types-dict),
[dictionary tutorial](http://learnpythonthehardway.org/book/ex39.html,)
[python pickle](https://docs.python.org/3/library/pickle.html), 
[python json](https://docs.python.org/3/library/json.html), 

- Networked data formats
- Python list programming tutorial (lists, tuples, dictionaries, serialization, ```range```)
- python json and pickle


Feb 18 *socket and application programming*
------
**chapter** 2.7

- Basic components of network applications (review)
- Python list demo
- DHA simulation (tcp client-server)

**A scrambled sequence**

>	[(4, 'e'), (1, 'b'), (2, 'c'), (5, 'f'), (0, 'a'), (3, 'd')]

**Demonstration of reassembling sequence in correct order.



---


Week 6
------

Feb 23 *socket and application programming*
------

- Review of networks application homework
- A DHA-like p2p application requirements (Part 1)
- [HW08 assigned](/457/hw/#hw-08) - P2P client application

Feb 25 *torrent-like distributed hash table*
------
- A DHA-like p2p application requirements (Part 2)


**A sample threaded application:**

{% highlight python %}
	

	""" python thread example """

	import threading
	import time

	GBL_COUNT = 0
	SHARED_DB = []

	class WriterThread(threading.Thread):
	    def __init__(self, threadID, name, e):
	        threading.Thread.__init__(self)
	        self.threadID = threadID
	        self.name = name
	        self.runtime = e

	    def run(self):
	        print "Starting " + self.name
	        while self.runtime.is_set():
	            threadLock.acquire() 
	            write_data()
	            threadLock.release() 

	class ReaderThread(threading.Thread):
	    def __init__(self, threadID, name, e):
	        threading.Thread.__init__(self)
	        self.threadID = threadID
	        self.name = name
	        self.runtime = e

	    def run(self):
	        print "Starting " + self.name   
	        while self.runtime.is_set():
	            threadLock.acquire() 
	            read_data()
	            threadLock.release() 

	def write_data():
	    global GBL_COUNT

	    GBL_COUNT += 1
	    time.sleep(.5)
	    print '\nw_GBL_COUNT => ', GBL_COUNT



	def read_data():
	    global GBL_COUNT
	    
	    GBL_COUNT -= 1           
	    time.sleep(.5)
	    print '\nw_GBL_COUNT => ', GBL_COUNT
	       

	""" SETUP """


	threadLock = threading.Lock()
	runtime_e = threading.Event()
	runtime_e.set()

	# Create new threads
	writer = WriterThread(1, "Writer", runtime_e)
	reader = ReaderThread(2, "Reader", runtime_e)

	# Start new Threads
	writer.start()
	reader.start()

	# Add threads to thread list
	threads = []
	threads.append(writer)
	threads.append(reader)


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

{% endhighlight %}



---


Week 7
------

Mar 01 
------
- **In-class** demonstration/lab threaded client server
- [p2p-threaded-client-server-demo.py](/assets/p2p-threaded-client-server-demo.py)

Mar 03 *Final network application*
------
- **In-class** discussion of p2p application requirements. [HW 9 assigned](/457/hw/)
- **critical** understanding of packet serializaton and deserialization


---


Week 8
------

Mar 08 *Application Layer review*
------
- See [midterm-study-guides](/457/midterm-review/)
- Midterm review
- p2p app questions

Mar 10 *Midterm exam*
------


---


Week 9
------

Mar 15 - 17 (spring recess)
------


---


*Week 10*
-------

Mar 22 *Transport Layer*
------

**chapter** 3.1, 3.2, 3.3, 3.4

- role of the transport layer
- services provided to the (upper) application layer
- udp ==> connectionless


Mar 24 *Transport Layer*
------
- multiplexing ==> "downward" sending of outgoing segments for routing at receiver
- demultiplexing ==> route "upward", the incoming segments to proper process (a socket with an assigned port)
- Connection-oriented protocols
- reliable data transmission
	* data integrity errors ==> checksums
	* data loss ==> ACKs and NAKs
- stop and wait or alternating bit protocol
- Go Back N (GBN) - pipelining
- Selective Repeat - pipelining
- TCP Overview


---

Week 11
-------

Mar 29 *Transport Layer: TCP*
------
- class not held due to illness
- [HW10 assigned](/457/hw/#hw-10) - Chapter 3 questions

Mar 31 *Transport Layer: TCP*
------
- Review==> Reliable Data Transfer:
	* checksum
	* timer
	* sequence number
	* acknowledgement (ACK)
	* negative acknowledgement (NAK)
	* window and pipelining

- Review==> Pipelining:
	* why ```stop and wait``` leads to under utilization
	* go-back-n (GBN) and cumulative acks
	* Demo: GBN applet
	* selective repeat (SR)
	* Demo: SR applet

**How does TCP achieve reliable data transfer?**

- TCP uses ```buffers```, ```variables```, and ```sockets```
- TCP uses pipelining with ```cumulative acks``` ~ receiver can buffer out of order segments yet this is implementation specific.
- TCP segment header
	* ACKS, seq number, receive buffer size, data

- TCP flow control
	* manage send and receive buffers
	* controlling what the receiver can **consume**
	* Demo: flow control applet

- TCP congestion control
	* not flow control but adjusts MSS in response to packet loss

---

Week 12
-------

Apr 05 *Network Layer*
------
- process to process communication (application and transport layers)
- host to host communication (network and link layers)
- forwarding and routing distinction
- forwarding tables
- virtual circuit network (connection-based network model)
- [HW11 assigned](/457/hw/#hw-11) - Wireshark Lab ==> IP Questions 1-9

Apr 07 *Network Layer*
------
- datagram network (connectionless network model)
- IP Datagrams
- IP fragments
- Routing algorithms


---

Week 13
-------

Apr 12 *Link Layer*
------

Apr 14 *Link Layer*
------


---

Week 14
-------

Apr 19 *Wireless Networks*
------

Apr 21 *Network Security*
------


---

Week 15
-------

Apr 26 *Network Security*
------

Apr 28 *Network Management*
------


---

Week 16
-------

May 03 *Multimedia Networking*
------

May 05 *Final Review*
------

Final Exam
-------

**Thursday May 12 @ 2:30 - 5:30p
