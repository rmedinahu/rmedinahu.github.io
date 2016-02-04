---
layout: page
title: 
permalink: /457/hw/fruit-basket/
---

	#!/usr/bin/python
	from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

	from urlparse import urlparse, parse_qs

	PORT_NUMBER = 8080

	"""
		This class extends BaseHTTPRequestHandler
		Its customized to only handle requests for fruit.
	"""

	class fruit_basket_handler(BaseHTTPRequestHandler):
		fruit_basket = {'oranges': 'yummy', 'grapes': 'wine is fine', 'apples': 'too tart', 'peaches': 'just peachee!', 'plums': 'great but no prunes'}
		
		#  Handler for the GET (fruit) requests
		def do_GET(self):

			"""
				How to get the query parameter?
				Look up the docs for BaseHTTPRequestHandler e.g., path

				Once you get the path you can use something like this to parse out the key sent by browser
				fruit_query = parse_qs(urlparse(self.path).query)
				f = fruit_query["fruitykey"] NOTE: this will return a list object so get the string like:
				f[0] would be the key entered in the form. Now you can do your lookup...
			"""

			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			
			# Send the html message back to client (browser)
			# This will obviously include the fruit message if the key matched!
			
			self.wfile.write('Shouldn\'t the server lookup your fruit?')
			
			return

	try:
		# Create a web server and define the handler to manage the
		# incoming request
		server = HTTPServer(('', PORT_NUMBER), fruit_basket_handler)
		print 'Started httpserver on port ' , PORT_NUMBER
		
		# Wait forever for incoming htto requests
		server.serve_forever()

	except KeyboardInterrupt:
		print '^C received, shutting down the web server'
		server.socket.close()