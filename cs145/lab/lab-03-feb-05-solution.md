---
layout: course_page
title: 
permalink: /145/lab03-sols/
parent_course: 145
---

Lab 03 - Feb 05 2016 - Solutions
---

{% highlight python %}
# lab-03-feb-05-solution.py

"""
This source code file contains solutions 
to the exercises in lab 3 (feb 5) as well 
as the solution to the "Lab Problems".

You can use for your reference and review.
"""

import random # Need this to use the randint function.

# string_in = raw_input('Enter a string:')
string_in = 'hola world'
# Assume I entered hola world at the above prompt.

# print the result from using various 
# string methods.

print 'string_in variable has value ==> ', string_in

print '\n\n****** STRING FUNCTIONS ****\n'
print 'find function says: ', string_in.find('d')
print 'index function says: ',string_in.index('d') 
print 'lower function says: ', string_in.lower()
print 'upper function says: ',string_in.upper()
print 'translate function deletes a\'s: ',string_in.translate(None, 'a')
print 'now is the time in title case:'
print 'title function says: ', 'now is the time'.title()

print '\n\n****** LISTS ****\n'
mylist = [10, 20, 30, 40, 41]

print 'mylist is:', mylist

print 'a subset of mylist[0:3]:', mylist[0:3]

print 'adding first and last item: ', mylist[0]+mylist[4]

mylist.reverse()
print 'mylist now reversed:', mylist

mylist[0] = random.randint(0, 100)
mylist[1] = random.randint(0, 100)
mylist[2] = random.randint(0, 100)
mylist[3] = random.randint(0, 100)
mylist[4] = random.randint(0, 100)

print 'mylist now has random ints: ', mylist

word = []  # Creates an empty list.
word.append('h')  # Insert a character 
word.append('e')  # Insert another character and so on.
word.append('l')  # Insert another character and so on.
word.append('l')  # Insert another character and so on.
word.append('o')  # Insert another character and so on.

print 'used the append function to build a list with 5 characters:', word


""" FUNCTION DEFINTION """
def echo():
	# string_input = raw_input('Your name? ')
	string_input = 'ram'
	print 'Hi', string_input



""" FUNCTION CALL """
print '\n\n Calling the echo() function:'
echo()


print '\n\n****** LAB PROBLEMS ****\n\n'

# string_in = raw_input('Enter a four letter word: ')
string_in = 'stop'
print 'Input reversed:', string_in[3]+string_in[2]+string_in[1]+string_in[0]

string_in = raw_input('Enter a file name: ')
i =  string_in.find('.')
print string_in[i:]

randoms = []
randoms.append(random.randint(1, 10))
randoms.append(random.randint(1, 10))
randoms.append(random.randint(1, 10))
randoms.append(random.randint(1, 10))
randoms.append(random.randint(1, 10))

print randoms
print 'average is', 
	(randoms[0]+randoms[1]+randoms[2]+randoms[3]+randoms[4]) / 5.0

{% endhighlight %}
