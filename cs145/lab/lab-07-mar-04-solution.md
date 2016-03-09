---
layout: course_page
title: 
permalink: /145/lab07-sols/
parent_course: 145
---

Lab 07 - Mar 04 2016 - Solutions
---

{% highlight python %}
# lab-07-mar-04-solution.py

from turtle import *
import random
screen = Screen()

def generate_random_nums(n):
	random_nums = []
	for i in range(n):
		random_num = random.randint(40, 100)
		random_nums.append(random_num)
	return random_nums


def draw_turtle_rect(w, h):
	penup()
	setpos(0, 200)
	pendown()

	lt(90)
	fd(h)
	lt(90)
	fd(w)
	lt(90)
	fd(h)
	lt(90)
	fd(w)

def draw_turtle_dots(n):
	penup()
	setpos(0,50)
	pendown()

	steps = 0
	while steps < n:
		color('black')
		setpos(steps * 10, 0)
		dot(5)
		steps = steps + 1


def plot_turtle_dots(list_to_plot):
	penup()
	setpos(-300, 0)
	pendown()

	WIDTH = 300.0
	scale = WIDTH/len(list_to_plot)
	dot_color = 'green'
	xcoord = -300
		
	for ycoord in list_to_plot:
		# draws line in gray
		color('gray')
		
		# move turtle to location at x, y
		setpos(xcoord, ycoord)
		color(dot_color)
		dot(10)

		# increment x position by scale
		xcoord += scale

def plot_turtle_rainbow_dots(list_to_plot):
	# reset() # this clears the window.

	penup()
	setpos(0, 250)
	pendown()
	write('RAINBOW DOTS!')
	penup()
	setpos(-300, 0)
	pendown()

	WIDTH = 300.0
	scale = WIDTH/len(list_to_plot)
	xcoord = -300
	
	for ycoord in list_to_plot:
		if ycoord > 89:
			dot_color = 'green'
		elif ycoord > 79:
			dot_color = 'orange'
		elif ycoord > 69:
			dot_color = 'blue'
		elif ycoord > 59:
			dot_color = 'yellow'
		else:
			dot_color = 'red'

		# draws line in gray
		color('gray')
		setpos(xcoord, ycoord - 200)
		color(dot_color)
		dot(10)

		xcoord += scale

# Main execution

# Exercise [1]
draw_turtle_rect(100, 100)

# Exercise [2]
draw_turtle_dots(40)

# Exercise [3]
random_nums = generate_random_nums(100)

# Lab Problem [4] 
plot_turtle_dots(random_nums)

# Lab Problem [5]
plot_turtle_rainbow_dots(random_nums)

done()


{% endhighlight %}