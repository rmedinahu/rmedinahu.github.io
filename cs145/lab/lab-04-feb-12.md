---
layout: page
title: 
permalink: /145/lab04/
---

Lab 04: Functions, Lists, & Rectangles(?) 
---
Feb 12 2016

> Complete [LAB 4 QUIZ](https://nmhu.desire2learn.com/d2l/le/content/28410/viewContent/270198/View?ou=28410){:target="_blank"} before beginning the lab.



**Topics and Skills To Be Covered**

* use string functions available in python
* use a random number generator function in python
* create, access, and process lists of numbers
* use slices to process *substrings*
* write and use very simple functions

Lab Exercises
---

---

**Create an empty .py file then try the following to make sure you understand lists:**

__REVIEWING LISTS__

**[1]**: Create a list of 5 random integers where each random number is between 1 and 100 inclusive, then print ONLY the first and last integer in your list.

>	You will need to use the random module in python.
>	
>	import random
>	random_num = random.randint(1, 100)

Add or assign items to a list using the list ```append``` function like so:

>	mylist = []
>	mylist.append(5)
> 	mylist.append(8)
>	and so on...

*Demo your code to instructor*

**[2]**: Using the list you created above, now swap the first and last numbers in the list. Print the list to verify the swap. 

*Demo your code to instructor*

**[3]**: Using the list you created above, print all the values EXCEPT for the first and last items.

*Demo your code to instructor*

Lab Problems
---
**You are beginning a new program so create a new empty .py file for the following problem.**

You are going to write a program that creates and processes a vector (a list) that stores information about a rectangular shape. Information about a rectangle simply includes: ```horizontal``` and ```vertical``` location in two dimensional space and the rectangle's ```width``` and ```height```. Altogether we need four pieces of information to represent a basic rectangle.

>	A rectangular shape can be represented as:
> 	rect = [x, y, w, h]

Your program should be able to ```generate``` a rectangle with four random integers where each integer coorelates to one of the four **properties** of a rectangle.

Your program should be able to perform certain computations on the vector. These are:

- scale (resize) the rectangle by a certain value input by the user
- translate (move) the rectangle by a certain value input by the user
- print information about the rectangle as in: ```location is 20, 20 and its size is 50 by 70```
- display the rectangle using ascii art techniques.

The overall flow of the program should be:

- On begin, the program will automatically ```generate``` a rectangular shape.
- The program should print the properties of the generated rectangular shape to the screen.
- Next the program will ask the user to resize the rectangle by providing a value to scale the width and height.
- The program will perform the rescaling and print the properties of the rectangle to verify its new properties.
- Next the program will ask the user to move the rectangle by providing a **new** horizontal and vertical location.
- The program will perform the translation and print the properties of the rectangle to verify its new properties.
- Lastly the program will display the rectangle with ascii art then exit: For example, a rectangle that is 5 by 7 could be printed on the console as follows:

>	- - - - -
>	|       |
>	|       |
>	|       |
>	|       |
>	|       |
>	|       |
>	|       |
>	- - - - -

**This program requires the following functions as specified below**:

```generate_rect()```: should RETURN a new list containing 4 random integers corresponding to ```[x, y, width, height]```

```print_rect(*a_rectangle*)```: should PRINT information about the rectangle given a rectangle variable (list) as its parameter.

```resize_rect(*a_rectangle*, *scale*)```: should RETURN a new rectangle (list) given a variable (list) and a scale value as its parameters. Scale means to increase the width and height by the same value. For any x and y ==> x*scale, y*scale

```translate_rect(*a_rectangle*, *new_x*, *new_y*)```: should RETURN a new rectangle (list) given a variable (list) and new horizontal and vertical locations as its parameters.

```display_rect(*a_rectangle*)```: should PRINT the rectangle given as a parameter on the console using ascii art as described above. **Note**: for this function we will ignore the horizontal and vertical position of the rectangle.



**Demo your program to the lab instructor, THEN upload to Desire2Learn for full credit**
---
