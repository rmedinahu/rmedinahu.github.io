---
layout: page
title: 
permalink: /145/lab03/
---

Lab 03: Strings, Lists, Simple Functions 
---
Feb 05 2016

This lab provides you an opportunity to explore string processing and, as a way to understand functions, we will use some built in string functions available in python. We will use simple lists as well as write our own very simple functions...just to give you the idea.

**Topics and Skills To Be Covered**

* use string functions available in python
* use a random number generator function in python
* create, access, and process lists of numbers and letters
* use slicing the process *substrings*
* write and use very simple functions

Lab Exercises
---
STRINGS

----

**Create an empty .py file to explore the following:

1. Visit [string docs](https://docs.python.org/2/library/stdtypes.html#string-methods). Try using the following string functions with a string input from the command line (use raw_input function).
	
[find](https://docs.python.org/2/library/stdtypes.html#str.find)

[index](https://docs.python.org/2/library/stdtypes.html#str.index)

*What is the difference between the two functions? What do both functions have in common?*

2. Use input from the command line to explore the following two methods.

[lower](https://docs.python.org/2/library/stdtypes.html#str.lower)
[upper](https://docs.python.org/2/library/stdtypes.html#str.upper)

*What is the difference between the two functions?*

3. Use input from the command line to explore the ```translate()``` method. Try using the function to delete all the 'a' characters from the input string.

[translate](https://docs.python.org/2/library/stdtypes.html#str.translate)

4. Try using ```title()``` function to convert a string like 'now is the time' to 'Now Is The Time'.

[title](https://docs.python.org/2/library/stdtypes.html#str.title)


LISTS

----

**For the following exercises create a simple list as follows:

> mylist = [10, 20, 30, 40, 41]

1. Print the substring of mylist up to and including the item with value 30. Use the slice operator.

2. Write a statement that prints the result of adding the first item in ```mylist``` with the last item in ```mylist```.

. Try using the ```reverse``` method to reverse ```mylist```.

[reverse](https://docs.python.org/2/library/stdtypes.html#mutable-sequence-types)

3. Use the ```random``` function to generate a random number. Use this function 5 times. Each time, assign the random number generated to successive successive items in ```mylist```. This will overwrite the existing value at each slot. Print ```mylist``` when done to view your new creation! 


FUNCTIONS

----

	def echo():
		in = raw_input('Your name? ')
		print 'Hi', in


1. Now use the echo() function in a program. E.g., Call it like:

> echo()


Lab Problems
---
Write a program that prompts the user for a string that contains exactly 4 characters. Your program should then output the string in reverse order. E.g., *stop* should be flipped to be *pots*

**Demo your program to the lab instructor**


Write a program that prompts the user for a filename containing a file extenstion in its name (e.g., fastprogram.py or myessay.doc) and prints the only the extension (with the . included).	

**Demo your program to the lab instructor**


Write a function that prints the average value from the following list of integers (please include the list statement in your function).


>	Name the function average_score
>	""" 
>		The purpose of the function should be to 
>		create a list of 5 numbers then print the 
>		average value of the 5 numbers in the list.
>	"""