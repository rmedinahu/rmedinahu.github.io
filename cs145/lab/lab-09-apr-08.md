---
layout: page
title: 
permalink: /145/lab09/
---

Lab 09: Programming Basics and Java
---

Apr 08 2016

>	NO QUIZ TODAY!

**Topics and Skills To Be Covered**

* Using arrays, loops, and conditionals in Java
* Getting user input using ```Scanner```
* Getting random number using ```Random```
* Reading and accessing [Java 8 documentation](http://docs.oracle.com/javase/8/docs/api/) and information on using [Scanner](http://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html)


Lab Exercises
---

---

**Create an empty .java file then try the following to make sure you understand the basic structure of a Java program.**

__Scanner and Basic Input__

**[1]**: Use the Scanner object to prompt the use for an integer. Store this integer in a variable then print the variable to the screen. Use a try / catch block to handle input errors. Your program should loop until the user has entered valid data (according to the prompt).

>	try {
>		System.out.print("Enter a number:");
>		int var_1 = user_input.nextInt();
>	
>	} catch (Exception e) {
>		// If user enters a value that is not an int, this catch block is executed.
>		System.out.println("Bad input. Try again.");
>	}

*Demo your code to instructor*

__Populating an Array__

**[2]**: Declare an array to contain N values of type double. Get N from the user (using Scanner of course). The program should populate the arrary with N random decimal point numbers in the range of 1 to 100.

*Demo your code to instructor*


__String_Building__

**[3]**: Write a short loop that iteratively asks the user for a single character. It then adds this character to the end of a string. The user should enter a special value to stop looping. After the loop, the program should print the newly built string to the screen.

*Demo your code to instructor*


Lab Problem / HW 13
---

**Please view [homework 13](/145/hw13/) to continue today's lab.**

**Homework 13 is due on Monday April 11 by 5pm**

---
