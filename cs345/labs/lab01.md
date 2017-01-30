---
layout: course_page
title: lab 1
permalink: /345/lab1/
parent_course: 345
---

### 2017-01-18

### Python Primer 1
Today's lab will focus on completing [pretest-20170117.py]({{ site.baseurl }}assets/cs345/pretest-20170117.py).

1. Clicking on link will download the python source code file for you to implement. 

2. **MODIFY AND RENAME FILE ACCORDING TO FORMAT EXPLAINED IN [syllabus](/345/syllabus/)**.

3. Submit your work to Desire2Learn dropbox before leaving lab. Do this even if you could not complete it.

### Resources
DSAP Textbook chapter 1

A potentially useful Python resource ==> [Learn Python the Hard Way](https://learnpythonthehardway.org/book/)


### Solution



{% highlight python %}
# v.20170117 pretest.py - solution.py

num_list = [7, 9, 2, 99, 544, 12, 49, 24, 0, -3, 7, 66, 20, 99, 7, 23, 7, 30, 88, 77]
first = 'guido'
last = 'rossum'

# Remove the pass statement then implement the following python function so that it swaps the values 
# in the parameters first and last then prints the variable named first. 

def swapper(first, last):
	print '\n', first, last
	tmp = first
	first = last
	last = tmp
	print first, last, '\n'

# Remove the pass statement then implement the following python function so that it prints the list parameter on one line separated by commas.
def printList(alist):
	print alist
	print '\n'


# Remove the pass statement then implement the following python function so that it prints the list parameter on one line in REVERSE order separated by commas.

def printListReversed(alist):
	print [alist[i] for i in range(len(alist)-1, -1, -1)]
	print '\n'

# Remove the pass statement then implement the following python function so that it swaps the first and last values from the list parameter.
# Then print the list to verify the first and last items were swapped. Use the above function to do this printing.

def swapFirstLast(alist):
	tmp = alist[-1]
	alist[-1] = alist[0]
	alist[0] = tmp
	printList(alist)

# Remove the pass statement then implement the following python function so that it locates the smallest number in alist.
# print the list
def findMin(alist):
	mymin = alist[0]
	for i in range(1, len(alist)):
		if alist[i] < mymin:
			mymin = alist[i]

	print 'MIN ==>', mymin
	printList(alist)

# Remove the pass statement then implement the following python function so that it locates the largest number in alist.
# Print the largest.
def findMax(alist):
	mymax = alist[0]
	for i in range(1, len(alist)):
		if alist[i] > mymax:
			mymax = alist[i]

	print 'MAX ==>', mymax
	printList(alist)

# Remove the pass statement then implement the following python function so that it reports the frequency of the parameter, target within the list called alist. 
# Print the frequency.
def findFrequency(alist, target):
	c = 0
	for i in alist:
		if i == target:
			c += 1
	print target, 'FREQ ==>', c


# ****** Test calls. Do not modify below this line ******

swapper(first, last)
printList(num_list)
printListReversed(num_list)
swapFirstLast(num_list)
findMin(num_list)
findMax(num_list)
findFrequency(num_list, 7)


{% endhighlight python %}
