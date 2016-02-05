---
layout: page
title: 
permalink: /145/lab03/
---

Lab 03: Strings, Lists, Simple Functions 
---
Feb 05 2016

> Complete [LAB 3 QUIZ](https://nmhu.desire2learn.com/d2l/le/content/28410/viewContent/269346/View?ou=28410){:target="_blank"} before beginning the lab.

This lab provides you an opportunity to explore string processing and, as a way to understand functions, we will use some built in string functions available in python. We will use simple lists as well as write our own very simple functions...just to give you the idea.

**Topics and Skills To Be Covered**

* use string functions available in python
* use a random number generator function in python
* create, access, and process lists of numbers
* use slices to process *substrings*
* write and use very simple functions

Lab Exercises
---
STRINGS

----

**Create an empty .py file to explore the following:**

**[1] Visit [string docs](https://docs.python.org/2/library/stdtypes.html#string-methods){:target="_blank"}. Try using the following string functions with a string input from the command line (use raw_input function).**
	
[find()](https://docs.python.org/2/library/stdtypes.html#str.find){:target="_blank"}

[index()](https://docs.python.org/2/library/stdtypes.html#str.index){:target="_blank"}

*What is the difference between the two functions? What do both functions have in common?*

**[2] Use input from the command line to explore the following two methods.**

[lower()](https://docs.python.org/2/library/stdtypes.html#str.lower){:target="_blank"}

[upper()](https://docs.python.org/2/library/stdtypes.html#str.upper){:target="_blank"}

*What is the difference between the two functions?*

**[3] Use input from the command line to explore the ```translate()``` method. Try using the function to delete all the 'a' characters from the input string.**

[translate()](https://docs.python.org/2/library/stdtypes.html#str.translate){:target="_blank"}

**[4] Try using ```title()``` function to convert a string like 'now is the time' to 'Now Is The Time'.**

[title()](https://docs.python.org/2/library/stdtypes.html#str.title){:target="_blank"}


LISTS

----

*For the following exercises create a simple list as follows:*

	mylist = [10, 20, 30, 40, 41]

**[1] Print the substring of ```mylist``` up to and including the item with value 30. Use the slice operator.**

**[2] Write a statement that prints the result of adding the first item in ```mylist``` to the last item in ```mylist```.**

**[3] Try using the ```reverse``` method to reverse ```mylist```.**

[reverse()](https://docs.python.org/2/library/stdtypes.html#mutable-sequence-types){:target="_blank"}

**[4] Use the ```random``` function to generate a random number. Use this function 5 times. Each time, assign the random number generated to successive items in ```mylist```. This will overwrite the existing value at each slot. Print ```mylist``` when done to view your new creation! Focus on using ```random.randint()```. Also don't forget to import the module! ==> ```import random```**

[random()](https://docs.python.org/2/library/random.html){:target="_blank"}

**[5] How to add items to a list? Use the ```append``` list function:**

	newlist = []  # Creates an empty list.
	newlist.append(59)  # Insert an integer to the end of the list.
	newlist.append(28)  # Insert another item and so on.

Try creating a new list (also provide a name of your choice) then populate with 5 letters of your choice. Then print the list to view your new list.


CUSTOM FUNCTIONS

----

*input the following function at the top of your program.*

	def echo():
		in = raw_input('Your name? ')
		print 'Hi', in


**[1] Now use the echo() function in a program. E.g., Call it simply as:**

	echo()


Lab Problems
---
Write a program that prompts the user for a string that contains exactly 4 characters. Your program should then print the string in reverse order. E.g., *stop* should be printed as *pots*. **NOTE:** the reverse function above won't work on str types. You don't need that for this little problem -- just *print* the string in reverse ...

**Demo your program to the lab instructor**


Write a program that prompts the user for a filename containing a file extenstion in its name (e.g., fastprogram.py or myessay.doc) and prints only the extension (with the . included).	

**Demo your program to the lab instructor**


Write a function that prints the average value from a list of exactly five random integers between 0-10 (please include the list statement in your function). Test your function be calling it multiple times. 


>	Name the function average_score
>	""" 
>		The purpose of the function should be 
>		1. create a list of 5 random numbers
>		2. print the average value of the 5 numbers in the list.
>	"""

**Demo your program to the lab instructor**

Have a nice weekend. Go Broncos!!!
---
