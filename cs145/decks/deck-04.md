---
layout: slide
theme: white
transition: slide
permalink: /145/deck-04/
---

<section data-markdown>
Introduction to Object Oriented Programming
----
CS 145

Deck 4 (Feb 10)
</section>

<section data-markdown>
Functions
----

**void functions**

- accepts no parameters **DOES NOT** return a value (void)
- accepts parameters **DOES NOT** return a value (void)

**fruitful functions**

- accepts no parameters **AND** returns a value (fruitful)
- accepts parameters **AND** returns a value (fruitful)

</section>

<section data-markdown>
No arguments, no return value
----

	def foo():
		z = 4
		print z ** 2

</section>

<section data-markdown>
Accepts arguments, no return value
----

	def foo(z):
		print z ** 2

</section>

<section data-markdown>
No arguments but returns a value
----

	def foo():
		z = 4
		square = z ** 2
		return square

</section>

<section data-markdown>
Accepts arguments AND returns a value
----

	def foo(z):
		square = z ** 2
		return square

</section>

<section data-markdown>
The addition function (fruitful) ...
----
>	z = x + y

	def add(x, y):
		z = x + y
		return z

</section>

<section data-markdown>
The area of a circle function (fruitful) ...
----
>	pi*radius^2
>	πr2

	def circle_area(r):
		area = 3.141592653589793 * r ** 2


</section>
