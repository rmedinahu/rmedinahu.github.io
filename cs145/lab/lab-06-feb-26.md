---
layout: page
title: 
permalink: /145/lab06/
---

Lab 06: Functions, Lists, and Conditionals 
---
Feb 26 2016

> Complete [LAB 6 QUIZ](https://nmhu.desire2learn.com/d2l/home/28410){:target="_blank"} before beginning the lab.



**Topics and Skills To Be Covered**

* The while loop
* Practice with functions.
* Writing boolean expressions and using boolean operators [docs](https://docs.python.org/2/library/stdtypes.html#boolean-operations-and-or-not){:targe="_blank"}
* Using ```if``` and ```if/else``` statements


Lab Exercises
---

---

**Create an empty .py file then try the following to make sure you understand lists, while loops and if/else statements:**

__REVIEWING LISTS AND STRINGS__

**[1]**: Define two separate functions. Each function will so the same thing -- it will print ```n``` asterisks across the screen. Ask the user for ```n```, then pass ```n``` to each function when you call it. 

```asterisk_string(n)``` will use string arithmetic to print ```n``` asterisks.

```asterisk_loop(n)``` will use a for loop to print ```n``` asterisks. This function should create a variable ```stars``` and assign it the empty string ```''```. The function should then use ```n``` as input to ```range``` then loop over ```range()``` ```n``` times, each time it loops it will *add* an asterisk to the ```stars``` variable. When the loop completes, print the variable ```stars```. It should display ```n``` asterisks in a row. This strategy is called a **SUMMMATION** and we use it alot in programming.

*Demo your code to instructor*


**[2]**: Define a function that takes one argument ```n``` and creates a list of ```n``` random numbers where each number is within the range 40 and 100. You must use a loop to construct the list. The function should **RETURN** the constructed list.

*Demo your code to instructor*


**[3]**: Define a function called ```min``` that takes one argument, a  list of integers, and **RETURNS** the minimum value in the list. The function must use a for loop with an if statement. Test this function with the output from the function you wrote in exercise [2].


**[4]**: Define a function called ```max``` that takes one argument, a list of integers, and **RETURNS** the maximum value in the list. The function must use a for loop with an if statement. Test this function with the output from the function you wrote in exercise [2].

*Demo your code for exercises [3] and [4] to instructor*


**[5]**: Define a function called ```generate_grade()```. The purpose of the function is to take one argument, an integer ```n```, and RETURN the grade as a string. A grade can be computed on the following scale.

>	A = n > 89
>	B = n > 79
>	C = n > 69
>	D = n > 59
>	F = n < 60

*Demo your code to instructor*


**[6]**: Define a function called ```guessing_game```. This function plays a guessing game with the user where the user continually guesses a number between 1 and 10 to see if it matches a predefined value. You will use a while loop to keep asking the user for their guess UNTIL they have guessed correctly. When they have guessed correctly, the while loop will end and the function will **RETURN** the number of tries the user attempted before guessing correctly. Be sure to print the results of the function to the user. Notes: a) generate a random number between 1 and 10 before beginning the while loop. b) Use the summation strategy to keep track of the number of attempts. 

*Demo your code to instructor*


Lab Problem
---
**You are beginning a new program so create a new empty .py file for the following problem.**

Extend the function in exercise [5] above so that allows the user to quit if they are tired of guessing. The range for the correct number will now be 1 through 20. Note: the while loop condition will now require a slightly more complicated ```condition```.


**Demo your program to the lab instructor, THEN upload this short program to Desire2Learn for full credit**

---
