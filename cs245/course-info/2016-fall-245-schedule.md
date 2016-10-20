---
layout: course_page
title: schedule
permalink: /245/schedule/
parent_course: 245
---

**Fall 2016 Schedule of Topics**

Jump to week[n] ==> [0](#week-0), [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6), [7](#week-7), [8](#week-8), [9](#week-9)

---
{:.green}
### 2016-10-18 Week 9

#### Readings

[Chapter 7 -- Searching and Sorting](http://math.hws.edu/javanotes/c7/s4.html)

#### Topics
- Midterm review
- Queue review
- Stacks and Queues in the real world

---

{:.gray}
### 2016-10-11 Week 8

> [Homework 7 assigned](/245/hw7)

#### Readings

[Chapter 7 -- Online Text](http://math.hws.edu/eck/cs124/javanotes7/c7/index.html)

#### Topics
- Stack review
- Midterm exam

---


{:.gray}
### 2016-10-04 Week 7

> [Homework 6 assigned](/245/hw6)

#### Readings

[Chapter 7 -- Online Text](http://math.hws.edu/eck/cs124/javanotes7/c7/index.html)

#### Topics
- Java *primitive* arrays vs. Java *ArrayList*
- Stack ADT and Queue ADT
- ```for : each``` construct


#### Demo Code (copy-paste-compile-execute)

{% highlight java %}
// week7.java

import java.util.ArrayList;

public class week7 {

	public static void main(String[] args) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		list.add(9);
		list.add(11);
		list.add(13);
		list.add(17);

		System.out.println("\n\nSIZE ==> \t" + list.size());

		System.out.print("VALUES ==> \t");
		
		for (int i = 0; i < list.size(); i++ ) {
			System.out.print(list.get(i) + ", ");
		}
		

		list.remove(0);

		System.out.println("\n\nREMOVED ITEM AT 0!\n\nSIZE ==> \t" + list.size());
		System.out.println("LIST @ 0 ==> \t " + list.get(0));

		System.out.print("VALUES ==> \t");
		
		// Using for:each construct.
		for (Integer item : list) {
			System.out.print(item + " ");
		}

		System.out.println("\n\n");

	}
}
{% endhighlight java %}


---

{:.gray}
### 2016-09-27 Week 6

#### Readings

[Chapter 7 -- Online Text](http://math.hws.edu/eck/cs124/javanotes7/c7/index.html)

#### Topics
- Stack ADT.
- Queue ADT.
- Java *primitive* arrays vs. Java *ArrayList*

---


{:.gray}
### 2016-09-20 Week 5

#### Readings

[Chapter 7 -- Online Text](http://math.hws.edu/eck/cs124/javanotes7/c7/index.html)

#### Topics
- Nested for loops.
- Two dimensional *primitive* arrays
- Java *primitive* arrays vs. Java *ArrayList*
- Stack v.2


---


{:.gray}
### 2016-09-13 Week 4


#### Topics
- Java *primitive* arrays
- Object oriented (information hiding, api)
- Stack

---


{:.gray}
### 2016-09-06 Week 3

#### Readings

[Functions, methods, subroutines](http://math.hws.edu/eck/cs124/javanotes7/c4/index.html)

[Objects and Classes](http://math.hws.edu/eck/cs124/javanotes7/c5/index.html)



#### Topics
- Object Oriented Programming
- Java arrays

---

{:.gray}
### 2016-08-30 Week 2

#### Readings

[Conditionals, loops, arrays](http://math.hws.edu/eck/cs124/javanotes7/c3/index.html)

[Strings Intro](http://math.hws.edu/eck/cs124/javanotes7/c2/s3.html#basics.3.3)


#### Topics
- Review Java basics (loops, conditionals, arrays)
- Review Java methods

---

#### 2016-08-23 | 25 Week 1 

#### Readings

[Conditionals, loops, arrays](http://math.hws.edu/eck/cs124/javanotes7/c3/index.html)

[Strings Intro](http://math.hws.edu/eck/cs124/javanotes7/c2/s3.html#basics.3.3)

#### Topics
- Review Java basics (loops, conditionals, arrays)
- Review Java methods
- Github accounts
- Project management (source "root", navigating the shell, compiling, executing)

---

#### 2016-08-18 Week 0

- Introduction 

```Homework``` ==> [Java Pre-assessment](/245/hw0/)

---




[comment]:### 2016-11-01 Week 10 chapter 7.4, searching, sorting 
[comment]:### 2016-11-08 Week 11 chapter 8, algorithm analysis, error handling
[comment]:### 2016-11-15 Week 12 chapter 9, linked lists, binary trees
[comment]:### 2016-11-22 Week 13 chapter 9, linked lists, binary trees
[comment]:### 2016-11-29 Week 14 

