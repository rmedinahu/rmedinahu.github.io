---
layout: page
title: 
permalink: /145/lab08/
---

Lab 08: First Java Programs
---

Apr 01 2016

>	NO QUIZ TODAY!

**Topics and Skills To Be Covered**

* Elements of basic Java program
* Writing simple Java programs
* Getting user input using ```Scanner```
* Getting random number using ```Random```
* Using ```if``` and ```if/else``` statements
* Using ```while``` loops
* Reading and accessing [Java 8 documentation](http://docs.oracle.com/javase/8/docs/api/)


[Scanner Docs](http://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html)

Lab Exercises
---

---

**Create an empty .java file then try the following to make sure you understand the basic structure of a Java program.**

__Hello World and Basic Output__

**[1]**: Using ```System.out.println()``` to send the string "Hello world!" to the screen.

*Demo your code to instructor*

__Scanner and Basic Input__

**[2]**: The Scanner class in the Java library allows programmers to read data from the screen (console). Below is an example that reads in an integer entered by the user. Add to your program from ex 1 to ask the user for their first name then print "Hello " along with whatever was entered for their name. Instead of ```nextInt()``` simply use ```next()``` to read the entire ```String```

>	import java.util.Scanner;  // Make the Scanner class available.
>
>
>	Scanner user_input = new Scanner( System.in );  // Create the Scanner.
> 	int users_number = 0;
>
>	System.out.print("Enter your favorite integer: ");
>	users_number = user_input.nextInt();
> 
>	System.out.println(users_number);
> 

*Demo your code to instructor*


**[3]**: Write a short segment that uses a while loop to print only even numbers between 1 and some random number up to and including 20. HINT: You will need an if statement within the loop to determine if number is an even number.

>	// A random number can be generated between 1 and 20 as follows:
>
>	(int)(Math.random()*20) + 1

*Demo your code to instructor*


Lab Problem/HW 11
---

**Snake Eyes Revisited (Create a new java source code file for this assignment)**


How many times do you have to roll a pair of dice before they come up snake eyes? You could do the experiment by rolling the dice by hand. Write a computer program that simulates the experiment. The program should report the number of rolls that it makes before the dice come up snake eyes. (Note: "Snake eyes" means that both dice show a value of 1.) 

HINTS: use the random function as noted above, requires a ```summation```, requires a ```while``` loop and an ```if statement```.


**This program is Due on Monday April 4 by 5pm**

---
