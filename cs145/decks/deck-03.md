---
layout: slide
theme: white
transition: slide
permalink: /145/deck-03/
---

<section data-markdown>
Introduction to Object Oriented Programming
----
CS 145

Deck 3 (Feb 3)
</section>

<section data-markdown>
Programming is Information Science
----
- programs **store** information (numbers, letters, strings)
- programs **process** information (calculations)
- programs solve specific problems and produce new information (algorithms)
- programs are highly structured problem solutions (step 1, step 2, step 3, ...)

</section>

<section data-markdown>
----

Programs are an EXPRESSION of your DEVISED solution to a problem.

Don't lose sight of the fact that the programmer must first have the solution in hand before it can become *computational* solution.

</section>


<section data-markdown>
Lists, strings, & functions 
----
- lists
- strings
- slices
- functions

</section>

<section data-markdown>
Lists
----
- a way to store and access **collections** of values.
- usually of the same type
- values have an order - there is a **first** item and a **last** item

</section>

<section data-markdown>
Lists are everywhere
----

List of scores:

67, 87, 99, 100, 40, 90

Order: 

**69** is the first item and **90** is the last

</section>

<section data-markdown>
List can contain any collection of values that can be stored in variables.
----

Floats 

7.9, 2.9, 50.987, 4.4, 0.8181

Characters

'd', 'x', 'f', 'r', 'r'

</section>

<section data-markdown>
Making a list in Python
----

	nums = [67, 87, 99, 100, 40, 90]

</section>

<section data-markdown>
Lists are a type
----
	>>> nums = [67, 87, 99, 100, 40, 90]
	>>> type(nums)
	>>> <type 'list'>

```nums``` is a type of list!

</section>

<section data-markdown>
Lists have a first item
----
	>>> nums = [67, 87, 99, 100, 40, 90]
	>>> nums[0]
	>>> 67

</section>

<section data-markdown>
Lists have a size or length
----
	>>> nums = [67, 87, 99, 100, 40, 90]
	>>> len(nums)
	>>>	6 

</section>

<section data-markdown>
Lists have an end
----
If you know its **length** you know its end.

	>>> nums = [67, 87, 99, 100, 40, 90]
	>>> num_count = len(nums)
	>>> nums[num_count-1]
	>>> 90

</section>

<section data-markdown>
List items have an **ADDRESS** or **INDEX**
----

	>>> nums = [67, 87, 99, 100, 40, 90]

The *index* of the value 67?

**0**

The *index* of the value 40?

**4**
</section>

<section data-markdown>
----
	>>> nums = [67, 87, 99, 100, 40, 90]
	>>> print nums[0]
	67
	>>> print nums[4]
	40
	>>> 
</section>

<section data-markdown>
Strings are really lists (of characters)
----
	>>> fakename = 'ram'
	>>> len(fakename)
	3
	>>> fakename[0]
	'r'
	>>> fakename[1]
	'a'
	>>> fakename[2]
	'm'

</section>


<section data-markdown>
List (pizza) slices
----
A slice is a SUBSET of a list. 


</section>

<section data-markdown>
Specifying which SUBSET you want in python
----

**some_list**[ *start* : *end* ]

Get subset of **some_list** BEGINNING at INDEX *start* UP TO but NOT INCLUDING INDEX *end*
</section>

<section data-markdown>
Example
----

phrase = ['s', 'n', 'o', 'w']

phrase[0:2]

['s', 'n']

phrase[:2]
	
['s', 'n']

phrase[:]

['s', 'n', 'o', 'w']

phrase[1:]

['n', 'o', 'w']

phrase[3:]

['w']

phrase[4:]

[] #  SUBSET DOESN'T EXIST!

<section data-markdown>
----
</section>
