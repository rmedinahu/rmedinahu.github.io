---
layout: page
title: 
permalink: /145/lab02/
---

cs145 Jan 29 2016 

Lab 02: Programming Expressions & Statements
===

This lab is intended to give you practice analyzing and developing solutions to small problems. It will provide hands on experience utilizing and understanding variables, types, and values. By the end of the lab you should be prepared to write a complete computer program that:

a. Performs a semi-useful function
b. Accepts and processes input from the *user*
c. Utilizes your knowledge of variable *types* and *values*
d. Requires basic math computations


Lab Exercises
===

## *1. About Type Coercion*

Type coercion means to change a variable's type from one to another. This is typically useful converting between **string**s an **integer**s or between **integer**s and **float**s.

```python
	# coerce a variable (or value) from one type to another

	# coerces parameter to integer type
	int(a-value-or-variable-here) 

	# coerces parameter to float type
	float(a-value-or-variable-here) 

	# coerces parameter to float type
	str(a-value-or-variable-here)
```

*Hint:* the python **type** function reports the type of variable or value given as a parameter:

```python	
	what_am_i = '7888'
	type(what_am_i)
	<type 'str'>
```

**Examples:**

```python
	user_input = '7888'
	# coerces a string to an integer
	total = int(user_input) 
	
	# coerces a string to a float
	average = float(user_input) 

	# coerces an integer to a string
	message = str(average) 
```

#### Experiment: 

Experiment with type coercion and using the **type** function to verify that your variable or value types are being changed. What happens when you try to coerce a word to an integer?

## *2. Printing output to screen*

**Use the print()** function


## *3. Getting input from screen (Terminal)*

*Hint:* use the *input* function to store what the user types at the screen. The input function *returns* a value of type string.

```python
	foo = input("Enter an integer here:")

	# what type is foo?
	type(foo)
	
	# Convert foo to an integer
	val = int(foo)
```
#### Experiment: 

Experiment using the input function by entering different types of information (e.g., a number, a word, a sentence, a bank account balance). 

## *4. Basic Math Operators*

#### Experiment: 

Experiment with a short program that asks the user for two numbers and prints the result of adding, substracting, multiplying, and dividing the two numbers.

## *5. Order of Operations (aka Operator Precedence)*

*Parentheses - Exponentiation - Mul|Div - Add|Sub THEN LEFT TO RIGHT*

#### Experiment:

Experiment arranging/combining various math operations into one *expression*. Notice the potential differences in answers depending on the order of operations.

E.g.,

```python
	# The result is not 5 (HUGE logic error)! What is it? How would you modify this to report the correct result, 5?
	
	average = 5 + 5 / 2 

```

## *6. Using the Modulo Operator*

Modulo operator (%) performs **integer division** on its operands but does not evaluate the quotient. It evaluates the remainder after performing the division. This is more handy than you think!

#### Experiment:

How would you compute the number of minutes and seconds if you only know the number of seconds? Try the following with different number seconds and make sure the results are correct.

```python
	seconds = 61
	minutes = seconds / 60
	leftover = seconds % 60
	print(minutes + ' mins ' + leftover + 'seconds')
```

## *7. Value Swapping*

#### Experiment: 

Sometimes we need to swap the values of two variables. How would you do that without losing value of either variable?

Lab Problems
===
1. Write a short program that accepts any number of seconds from the user and reports the number of:
	- seconds
	- minutes
	- hours
	- days

*Hint:*

- secs-day = 86400
- secs-hour = 3600
- secs-min = 60

Example output:

*Enter number of seconds:* **100000** (I enter 100000)

*Computed as:* **1 day, 3 hours, 46 minutes, 40 seconds**


#### TEST!

*You can use the following to validate your answer. The result of this expression should be exactly equal to the input.


*(day * 86400) + hours(3600) + (minutes*60) + seconds*



Submit ONE file to D2L dropbox. This file should contain your program for the LAB problem. Don't forget to put your name comments at the top of the program. See syllabus for detailed requirements about this.







