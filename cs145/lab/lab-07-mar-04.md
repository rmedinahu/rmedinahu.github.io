---
layout: course_page
title: 
permalink: /145/lab07/
parent_course: 145
---

Lab 07: The Turtle Returns [(solutions)](/145/lab07-sols/)
---

Mar 04 2016

>	NO QUIZ TODAY!

**Topics and Skills To Be Covered**

* The while loop
* Practice with functions.
* Writing boolean expressions and using boolean operators [docs](https://docs.python.org/2/library/stdtypes.html#boolean-operations-and-or-not){:targe="_blank"}
* Using ```if``` and ```if/else``` statements
* Python turtle graphics

[turtle docs](https://docs.python.org/2.6/library/turtle.html)

Lab Exercises
---

---

**Create an empty .py file then try the following to make sure you understand lists, while loops and if/else statements:**

__BASIC TURTLE__

**[1]**: Use the following code to initialize a turtle window. Then, define a function that accepts a width and height and uses turtle to draw a rectangle. You will use ```lt(degrees)```, ```fd(integer)```, and ```color(color string)```. Call the function with width and height values of your choice. **This exercise inspired by M. Aguilar. :)**

>	from turtle import *
>	screen = Screen()
>	
>	# Function defs here...
>
>	# Turtle program execution begins here...	
>
>	done()

*Demo your code to instructor*

__WHILE LOOPS__

**[2]**: Define a function that accepts one integer argument ```n```. The function should loop ```n``` times. Each time it loops it advances the turtle forward 10 units then draws a dot in any color you choose. Call the function with different values for ```n```

USE: ```dot(size optional)``` and ```fd()```

*Demo your code to instructor*


**[3]**: Define a function that returns ```n``` random values between 40 and 100.


**[4]**: Define a function that plots values in a list using turtle. The function should accept a list as its only argument. It should then plot the list from left to right where the height of the plot point is determined by each value in the list. Each point must be printed with a dot. Use your function from exercise 3 to generate the list!

USE: ```dot()```, ```setpos(x, y)```, ```color()```

*Demo your code for exercises [3] and [4] to instructor*


Lab Problem
---

Extend the function in exercise 4 so that it prints the dot in a different color depending on the value of the list.

>	A = n > 89 # color should be green
>	B = n > 79 # color should be orange
>	C = n > 69 # color should be blue
>	D = n > 59 # color should be yellow
>	F = n < 60 # color should be red

**Demo your program to the lab instructor, THEN upload this short program to Desire2Learn for full credit**

---
