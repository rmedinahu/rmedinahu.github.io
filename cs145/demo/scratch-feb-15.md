---
layout: code
title: 
permalink: /145/demo/scratch-feb-15/
---

{% highlight python %}
# scratch-feb-15.py

"""
rectangle represented by a list of four values:
	
	[ xloc, yloc, width, height ]

Demonstration code used in class.

- illustrates fruitful function w/no params
- illustrates fruitful function w/params
- illustrates void function w/params
"""

""" FUNCTION DEFINITIONS """

# Fruitful function without params
def generate_rect():
	r = []

	# Want different sizes? Use randint with different ranges!
	r.append(random.randint(1, 5))
	r.append(random.randint(1, 5))
	r.append(random.randint(1, 5))
	r.append(random.randint(1, 5))

	return r

# Fruitful function with two params
def resize_rect(a_rectangle, scale):
	a_rectangle[2] = a_rectange[2] * scale
	# incomplete scale the height too!
	return a_rectangle

# Void function with one param
def print_rect(a_rectangle):
	print 'xloc', a_rectangle[0]
	print 'yloc', a_rectangle[1]
	print 'width', a_rectangle[2]
	print 'height', a_rectangle[3]



""" MAIN EXECUTION BEGINS HERE """


# Function calls:
rectangle = generate_rect() # Make a rectangle then store return value in variable rectangle

print_rect() # print rectangle information

rectangle = resize_rect(rectangle, 5) # resize rectangle, then update rectangle with returned value

print_rect() # print rectangle information -- should have new width and height right?
{% endhighlight %}








