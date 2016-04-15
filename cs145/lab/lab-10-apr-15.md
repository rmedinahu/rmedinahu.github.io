---
layout: page
title: 
permalink: /145/lab10/
---

Lab 10: Loops, Conditionals, Methods, and First Objects
---

Apr 15 2016

>	NO QUIZ TODAY!

**Topics and Skills To Be Covered**

* Using arrays, loops, and conditionals in Java
* Writing ```static``` functions in Java
* Building and using a Java class of your own.
* Reading and accessing [Java 8 documentation](http://docs.oracle.com/javase/8/docs/api/) and information on using [Scanner](http://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html)


Lab Exercises
---

---

**Create an empty .java file then try the following to make sure you understand the basic structure of a Java program.**

__Writing a static void function__

**[1]**: Write a subroutine named "stars" that will output a line of stars to standard output. (A star is the character "*".) The number of stars should be given as a parameter to the subroutine. Use a for loop. For example, the command "stars(20)" would output

>	********************

*Demo your code to instructor*

__Using a static function from main__
	
**[2]**: Write a main() routine that uses the subroutine that you wrote for exercise 1 to output 10 lines of stars with 1 star in the first line, 2 stars in the second line, and so on, as shown below.

>	*
>	***
>	****
>	*****
>	******
>	*******
>	********
>	*********
>	**********
>	***********

*Demo your code to instructor*


__Writing a static fruitful function__

**[3]**: Write a function named ```countChars``` that has a String and a char as parameters. The function should count the number of times the character occurs in the string, and it should return the result as the value of the function. Get the string from the user. Note that this problem requires the summation pattern.

*Example*

>	Enter a string: hello
>	Enter a character to count: l
>	l appears 2 times in the string hello.

*Hint*

The ```String``` class [docs](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) has a method called ```charAt(int index)```. It also has a method that returns a String's length ==> ```length()```

>	String s = "whoa";
>	System.out.println(s.length()); // Should print 4

You can use these two methods to 1) set up a for loop and 2) implement the summation pattern.

*Demo your code to instructor*


__Writing a static fruitful function with multiple parameters__

**[4]**: Write a subroutine with three parameters of type int. The subroutine should determine which of its parameters is smallest. The value of the smallest parameter should be returned as the value of the subroutine. Call this function from ```main``` with three integers entered by the user. Make sure you use a try/catch block to handle input that is not an integer (see [lab09](/145/lab09/) for example of this.)

*Example*

>	Enter number 1: 7
>	Enter number 2: 1
>	Enter number 3:	9
>	Smallest number is 1

*Hint*: **Use an if/else chain**


__Using custom Java classes__

**[5]**: Create a new directory in your working folder named ```mosaic-program```. Then download the following files to the newly created folder. Navigate to the new folder and compile and run the program RandomMosaicWalk.

[RandomMosaicWalk.java](http://math.hws.edu/javanotes/source/chapter4/RandomMosaicWalk.java)

[Mosaic.java](http://math.hws.edu/javanotes/source/chapter4/Mosaic.java)

[MosaicPanel.java](http://math.hws.edu/javanotes/source/chapter4/MosaicPanel.java)

Your done!!!

Lab Problem 
---

see [homework 15](/145/hw15/)


---
