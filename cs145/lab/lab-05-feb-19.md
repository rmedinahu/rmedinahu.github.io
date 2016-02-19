---
layout: page
title: 
permalink: /145/lab05/
---

Lab 05: Functions, Lists, & Loops 
---
Feb 19 2016

> Complete [LAB 5 QUIZ](https://nmhu.desire2learn.com/d2l/le/content/28410/viewContent/271043/View){:target="_blank"} before beginning the lab.



**Topics and Skills To Be Covered**

* Practice with functions.
* create, access, and process lists of numbers
* using random module
* using ```range``` function [[docs]](https://docs.python.org/2/tutorial/controlflow.html#the-range-function){:target="_blank"}
* Basic ```for``` loops with lists [[docs]](https://docs.python.org/2/tutorial/controlflow.html#for-statements){:target="_blank"}

Lab Exercises
---

---

**Create an empty .py file then try the following to make sure you understand lists:**

__REVIEWING LISTS__

**[1]**: Create a list of 5 random integers between 1 and 20.

>	You will need to use the random module in python.
>	
>	import random
>	random_num = random.randint(1, 100)

*Move on to next step*

**[2]**: Using the list above, change each value in the list by adding 1. Print the list to verify its new sequence. 

*Demo your code to instructor*

**[3]**: Create 3 different lists of integers numbered from 1 to some random number between 1 and 20. Hint: use the ```range``` function.

Print the length of each list and the list itself. How are they different?

*Demo your code to instructor*

**[4]**: write a function that accepts one argument ( a list) and prints each item in the list on separate line. You will need to ask the user for the size of a list and then create the list using the ```range``` function. Pass this list to your function. Why is this difficult? Is it impossible? 


__FOR LOOPS__! First take a quick look at the docs for the FOR statement. [docs](https://docs.python.org/2/tutorial/controlflow.html#for-statements){:target="_blank"}

>	for i in LIST:
>		# do some statement

Now try exercise 4 using a for loop. You will implement the for loop in the function.

*Demo your code to instructor*


**[5]** define a function that will print ```n``` asterisks across the screen. Ask the user for ```n```, then pass ```n``` to your function. Your function should create a variable ```stars``` and assign it the empty string ```''```. The function should then use ```n``` as input to ```range``` then loop over ```range()``` ```n``` times, each time it loops it will *add* an asterisk to the ```stars```. When the loop completes, print the variable ```stars```. It should display ```n``` asterisks in a row.

Lab Problem
---
**You are beginning a new program so create a new empty .py file for the following problem.**

You are going to write a program that accepts two pieces of input from the user: a width and a height of a rectangle. Your program should then print the ascii art of the rectangle as specified by width and height. You are required to write a function that will do this for any sized rectangle. Name this function ```rascii``` 

*How many arguments should the ```rascii``` function have?*


**HINT**: You can do the art with three loops (one to print the top, one to print the height, and one to print the bottom). This can be done in one loop of course but I suggest using three for this exercise.

For example, a rectangle that is 5 by 7 could be printed on the console as follows:

>	- - - - -
>	|       |
>	|       |
>	|       |
>	|       |
>	|       |
>	|       |
>	|       |
>	- - - - -


**Demo your program to the lab instructor, THEN upload to Desire2Learn for full credit**
---
