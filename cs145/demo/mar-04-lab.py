# mar-04-lab.py
import random
from turtle import *
screen = Screen()

# Function defs here...

def gen_randoms(n):
	random_nums = []
	count = 0
	while count < n:
		r_num = random.randint(40, 100)
		random_nums.append(r_num)
		count = count + 1

		
def draw_rect(w, h):
	# turtle time!!!!
	color('blue')
	fd(w)

def dots(n):
	
	colormode(255)
	color((180, 180, 180))
	count = 0
	while count < n:
		fd(10)
		dot(2)
		count += 1
	

# Turtle program execution begins here...	

# draw_rect(40, 50)
dots(7)

done()