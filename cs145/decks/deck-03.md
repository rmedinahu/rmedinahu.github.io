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

Deck 3
</section>

<section data-markdown>
Lists, strings, & functions (Feb 3 )
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
A slice is a sublist of a list. 
	>>> phrase = ['s', 'n', 'o', 'w']
	>>> phrase[0:2]
	['s', 'n']
	>>> phrase[:2]
	['s', 'n']
	>>> phrase[:]
	['s', 'n', 'o', 'w']
	>>> phrase[1:]
	['n', 'o', 'w']
	>>> phrase[3:]
	['w']
	>>> phrase[4:]
	[]
	>>> phrase[3:]
	['w']

</section>

<section data-markdown>
----
</section>
