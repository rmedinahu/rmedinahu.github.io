---
layout: course_page
title: Final Exam Study Guide
permalink: /245/final-study-guide/
parent_course: 245
---

## Overview
The final exam will be given online in D2L. This exam is cumulative therefore [questions](#midterm-questions) from the midterm exam will be included in addition to the new topics we have covered since then. This guide is designed to help you focus on the topics to be assessed.

## New Topics:

### Relevant Textbook Chapters ==> chapter 7, chapter 8, chapter 9

### Topics



- Sorting **Understand how the following algorithms work. I highly recommend that you practice answering the questions that are linked.**
	- bubble sort [try the quiz](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html)
	- selection sort [try the quiz](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html)
	- insertion sort [try the quiz](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html)
- Searching
	- linear search vs. binary search
- Data Structures (ADT's)
	- queues
	- stacks
	- primitive vs. ArrayList class
	- linked lists
	- benefits of a linked list over a primitive array
- Programming Concepts:
	- recursion: **Identify** base case vs. recursive case
	- copy by value vs. copy by reference: **a variable's address is DISTINCT from its value**
	- algorithm efficiency: **n2 vs log n**
	- ```for: each``` construct
	- exception handling, robust programs, ```try/catch``` blocks
	- program correctness



## Midterm Questions:

In computer programming, what does the concept of information hiding refer to?

- [x] hiding the implementation to manage complexity
- hidden variables in a list
- password encryption
- hiding algorithms from the public


What does API stand for?

- application parameter instance
- application programming inactive
- [x] application programming interface
- application programming implementation


What is the purpose of an API?

- to assist programmers with using other libraries
- to constrain the types of behaviors defined for a class
- to provide a set of possible actions on an object
- [x] all of the above


What does ADT stand for?

- application data transfer
- application data type
- [x] abstract data type
- none of the above


Which of the following kinds of data is NOT an ADT?

- stack
- [x] int
- queue
- array


Analyze the following code. What is the value printed on the screen after this code completes? (You can assume the code compiles.)

{% highlight java %}
ArrayList<Integer> list = new ArrayList<Integer>();
list.add(1);
list.add(2);
list.add(3);
list.add(5);
list.add(2);

System.out.println( list.get(list.size() - 1) )

1
X2
3
5
nothing is printed because an index out of bounds error occurs.


Analyze the following code. What is the value printed on the screen after this code completes? (You can assume the code compiles.)

int LIST_SIZE = 5
int[] list = new int[LIST_SIZE];
list[0] = 1;
list[1] = 2;
list[2] = 3;
list[3] = 5;
list[4] = 2;

System.out.println( list[LIST_SIZE] );
{% endhighlight %}

- 1
- 2
- 3
- 5
- [x] nothing is printed because an index out of bounds error occurs.


Analyze the following code. What is the value printed on the screen after this code completes? (You can assume the code compiles.)

{% highlight java %}
char[] message = {'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'};

for (int i = message.length - 1; i > -1; i--) {
	if (message[i] != ' ') {
		System.out.print(message[i]);
	} else {
		System.out.print("*");
	}
}
System.out.println();
{% endhighlight %}

- dlrow olleh
- hello*world
- [x] dlrow*olleh
- hello world
- nothing is printed because an index out of bounds error occurs.


MidtermStack implements a stack. What is the value printed on the screen after this code completes? (You can assume the code compiles.)

{% highlight java %}
MidtermStack stack = new MidtermStack();
stack.push(90);
stack.push(80);
stack.push(70);

int t = stack.top();
int u = stack.pop();
int v = stack.top();
System.out.println(t + " - " + u +  " - " + v);

{% endhighlight %}
- 70 - 80 - 90
- 90 - 80 - 70
- 90 - 90 - 80
- [x] 70 - 70 - 80


Analyze the following code. What is the value printed on the screen after this code completes? (You can assume the code compiles.)

{% highlight java %}
char[] message = {'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'};
for( char i : message ) {
	if (i == 'l') {
		System.out.print(1);
	} else if (i == 'o') {
		System.out.print(0);
	} else {
		System.out.print(i);
	}
}
{% endhighlight %}

- hello world
- [x] he110 w0r1d
- 012345678910
- 109876543210
- nothing is printed because an index out of bounds error occurs.


What is the advantage of a dynamic array over a regular array?

- dynamic arrays are difficult to implement and not usually used
- there are no advantages because they are the same thing with different names
- [x] a dynamic array has no upper limit
- a dynamic array has a fixed size



Analyze the following code that processes a 6X6 matrix. What is the value printed on the screen after this code completes? (You can assume the code compiles.)

{% highlight java %}
int num_rows = 6;
int num_cols = 6;

// Creating a 6 x 6 two dimensional array of .'s

/* Example:
......
......
......
......
......
......
*/

char[][] pic = new char[num_rows][num_cols];
for (int i = 0; i < num_rows; i++) {
	for (int j = 0; j < num_cols; j++) {
		pic[i][j] = '.';
	}
}

// Printing a pattern
for (int i = 0; i < num_rows; i++) {
	for (int j = num_cols-1; j >= 0; j--) {
   		if (i == j) {
   			System.out.print('*');
   		} else {
   			System.out.print(pic[i][j]);
   		}
   	}
   	System.out.println();
}

X.....*
....*.
...*..
..*...
.*....
*.....

*.....
.*....
..*...
...*..
....*.
.....*

.....*
.....*
.....*
.....*
.....*
.....*

*.....
*.....
*.....
*.....
*.....
*.....
{% endhighlight %}


Analyze the following program that uses Gradebook. What is printed on the screen after this program completes? (You can assume the code compiles.)
{% highlight java %}
class Gradebook {
	int[] grade_data = {1, 2, 3, 5, 7, 11, 13};

	public int capacity() {
		return grade_data.length;
	}

	public void expand() {
		int[] t = new int[grade_data.length * 2];

		for (int i = 0; i < grade_data.length; i++) {
			t[i] = grade_data[i];
		}
		
		grade_data = t;
	}

	public static void main(String[] args) {
		Gradebook g = new Gradebook();
		g.expand();
		System.out.println( "Gradebook Size: " + g.capacity() );
	}
}

{% endhighlight %}

- Gradebook Size: 0
- Gradebook Size: 7
- [x] Gradebook Size: 14
- nothing is printed because an index out of bounds error occurs.
