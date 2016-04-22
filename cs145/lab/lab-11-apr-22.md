---
layout: course_page
title: 
permalink: /145/lab11/
parent_course: 145
---

Lab 11: Object Oriented Programming
---

Apr 22 2016 

>	NO QUIZ TODAY!

**Topics and Skills To Be Covered**

* Building and using simple Java classes and objects
* Writing ```static``` functions in Java
* Writing ```non-static``` class methods
* Writing ```getter``` and ```setter``` methods

[Java 8 documentation](http://docs.oracle.com/javase/8/docs/api/)

[Scanner](http://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html)


Lab Exercises
---

---

**A. Create a new folder to contain today's object oriented program files.**

Creating a Java class file (without a main)
----

**[1]**: Copy and paste the code in [AsciiRectangle.java](/cs145/demo/java/ascii-art-application/AsciiRectangle.java) into a file of the same name in your application folder. Do the same for [AsciiArtGenerator.java](/cs145/demo/java/ascii-art-application/AsciiArtGenerator.java)

a. **Remove** the properties ```xcoord``` and ```ycoord```.

b. Update the ```CONSTRUCTOR``` to reflect the fact that the rectangle class does not have xcoord and ycoord properties.

c. Use the ```AsciiArtGenerator``` class to test your changes.

*Demo your code to instructor*

Adding ```getter``` methods to your AsciiRectangle class.
----
	
**[2]**: Getter methods provide a way for other programs to retrieve properties from an object. Write two class methods in ```AsciiRectangle``` that return the width and height of a rectangle respectively. Test these methods using ```AsciiArtGenerator.java``` as you did in exercise 1.

*Demo your code to instructor*

Adding ```setter``` methods to your AsciiRectangle class.
----

**[3]**: Setter methods provide a way for other programs to set the values of properties that belong to an object. Write two class methods in ```AsciiRectangle``` that set the width and height of a rectangle respectively. Test these methods using ```AsciiArtGenerator.java``` as you did in exercise 2. Note: setter methods typically do not return a value but instead take a parameter that is used to assign a value to an object's property.

*Demo your code to instructor*


Adding a new object method
----

**[4]**: Write a new method to the ```AsciiRectangle``` class that prints the rectangle on the screen. This version should print the rectangle filled in with stars. Again test this new method as before.

*Example output (a rectangle that is ```6 X 5```*:

>	******
>	******
>	******
>	******
>	******

*Demo your code to instructor*

Add a second ```DEFAULT``` contstructor
----

**[4]**: A default constructor for a class takes no arguments but simply initializes an object's properties with default values. For example, rectangles constructed with the default constructor could set the width to 10 and the height to 5. Add a default constructor to the ```AsciiRectangle``` class with default values of your choice. Test this new constructor as before.

*Demo your code to instructor*


Lab Problem 
---

see [homework 17](/145/hw17/)


---
