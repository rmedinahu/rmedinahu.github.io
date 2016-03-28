# hw09.py

import random

from turtle import *

screen = Screen()


# Main Execution
shape('circle')
penup()
color('green')
v = 1

while True:
	if position()[0] < -300:
	  v = 1
	  
	elif position()[0] > 300:
	  v = -1
	  
	
	forward(1*v)

