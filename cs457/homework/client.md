---
layout: course_page
title: 
permalink: /457/hw/client/
parent_course: 457
---

	#!/usr/bin/env python

	"""Simple client application"""

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
	#	 AF_INET = ipv4 addressing 
	#	 SOCK_STREAM = transport protocol (tcp)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	# connect to a server at host on port
	s.connect((host,port))

	# send data to server 
	s.send('Message from me')

	# wait for/read in response 
	data = s.recv(size) 

	# close connection
	s.close()

	# what'd we get?
	print '\nServer RESPONSE:\n> ', data
