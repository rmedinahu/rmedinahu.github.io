---
layout: slide
theme: black
transition: slide
permalink: /145/deck-02/
---

<section data-markdown>
Introduction to Object Oriented Programming
----
CS 145

Deck 2
</section>

<section data-markdown>
Jan 27 Expressions and statements
----
- variables, types, and values
- categories of programming instructions (input, output, math, conditionals, repetition)
- basic math operators (+, -, *, /, %, **)
- assignment operator
- expressions and statements
- i/o statements (raw_input, print)
- syntax errors vs. execution (run time or exception) errors
- semantic errors
- the programming process
- hw02 assigned

</section>

<section data-markdown>
Variables
----
- a name we use to refer to a value
- also a name we use to refer to a memory location

- variables have a **type** AND a **value**

</section>

<section data-markdown>
Types
----
- integer (whole number)
	- *5*, *6005*, *0*

- float (fraction)
	- *6.9*, *3.0*, *3.14*

- character (single alphanumeric symbols)
	- *'a'*, *'7'*

- string (one or more characters -- "strung together"
	- *'good morning foo dog'*, *'hello robot 8'*

- list (a group or set of values of some type referred to by a variable)
	- *('red', 'green', 'purple')*
	- A string is really a "list" of characters (that probably spell a word or sentence)
	
</section>

<section data-markdown>
Variables and Types Together
----

	# Finding the average 
	scores = 943
	students = 12
	average = scores/students
	print(average)

Result ==> **78**

INTEGER division! Why?

</section>

<section data-markdown>
Use a float for fractional expressions
----

	# Finding the average 
	scores = 943.0
	students = 12
	average = scores/students
	print(average)

Result ==> **78.58333333333333**

FLOATING POINT precision! Why?

</section>

<section data-markdown>
Operators
----

- math operators: ** +, -, *, /, % **

- assignment operator: **=**
	- "assigns" EXPRESSION on the RIGHT to VARIABLE on the LEFT **RIGHT TO LEFT**

		x = 20
		
		y = 90.1
		
		z = x + y

</section>

<section data-markdown>
Expressions and Statements
----
- Expressions consist of tokens (variables, operators, and values) that are **evaluated**

- Statements consist of expressions or functions that trigger an action in the machine.
	- Statement is an *INSTRUCTION* or *HAS AN EFFECT*

Expression:
	
	3.14 * 9 ** 2

Statement:

	# ** is the exponentiation operator 
	area = 3.14 * 9 ** 2

</section>

<section data-markdown>
I/O Statements
----

**Input** Getting data in:
	
	password_input = raw_input('Enter your password: ')

**Output** Pushing data out:

	print(password_input + ' is incorrect!')

</section>

<section data-markdown>
BUGS: Syntax, Exceptions, Semantic Errors
----
- **Syntax**
	- program contains one or more statements that break the rules of the language
	- cannot be compiled nor interpreted
	
- **Exceptions** (aka *runtime errors*, *blue screen of death*, *epic failure*, etc.)

	- program has correct syntax but encounters an error during execution
	- cannot be executed
	
- **Semantic or Logic Error**
	
	- program executes but does not work as intended. 
	- E.g., A respirator control system stops when it shouldn't have  

</section>

<section data-markdown>
Programming Process or Debugging
----
1. devise a solution to a problem that can be solved by a computer
2. express the solution as a sequence of instructions in a file using a programming language
3. compile the program or source code
4. IF SYNTAX ERROR - return to step 2
5. execute ("run") the program
6. IF RUNTIME EXCEPTION - return to step 2
7. verify program is correct by testing it with different values or input
8. IF LOGIC ERROR - return to step 2
9. Take a break.

</section>

<section data-markdown>
Development Hints
----
- ALWAYS try to break the problem down into smallest steps possible, *THEN* see if any of those steps can be combined. **BREAK IT DOWN THEN BUILD IT**
- learn and use **keyboard shortcuts**
- minimize distractions from other apps on your computer while coding
- keep your browser handy to display documentation
- *NOTICE the details!* Programs and programming require **detail oriented* attention

</section>


	
