#!/usr/bin/python

import thread
import time

import math
import random


def calc_area():
	i = 0
	while i < 1000:
		time.sleep(2)
		r = random.randint(1, 100)
		area = 3.14 * r ** 2
		print '************************************', area
		i = i + 1

def read_pass():
	f = open('john.txt')
	data = f.read(1)
	while data:
		print data.upper()
		data = f.read(1)

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   100/delay
   while count < 1000:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )





# Create two threads as follows
try:
	thread.start_new_thread( calc_area, () )
	thread.start_new_thread( read_pass,() )
   
   
except:
   print "Error: unable to start thread"

while 1:
   pass