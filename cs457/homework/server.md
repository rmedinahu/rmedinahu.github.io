---
layout: course_page
title: 
permalink: /457/hw/server/
parent_course: 457
---


	#!/usr/bin/env python

	"""Simple server application"""

	import socket
	#  server host (local machine)
	host = 'localhost' 

	#  machine port
	port = 7000

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

	#  poll for incoming connections then send response
	while 1:
	    print 'Server ready, willing and able!'

	    # waits for connection 
	    # then returns a tuple representing socket connection object
	    client, address = s.accept()

	    print 'Message from', address
	    
	    data = client.recv(size) # reads in the payload
	    if data: 
	        client.send('Server received this from you: \n' + data) # sends it back
	    client.close() # close the connection

