---
layout: course_page
title: schedule
permalink: /345/schedule/
parent_course: 345
---

**Spring 2017 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6), [7](#week-7), [8](#week-8), [9](#week-9), [11](#week-11), [12](#week-12), [13](#week-13), [14](#week-14)

---

{:.green}
### 2017-04-17 Week 14

### Trees

#### Readings
- **CHAPTER 8** ==> DSAP (Data Structures and Algorithms in Python)
- **Online Resource** ==> [Trees](http://interactivepython.org/runestone/static/pythonds/Trees/toctree.html)


#### Topics
- binary trees review
- binary tree traversal ```preorder``` ```inorder``` ```postorder```

#### Custome Iterator for a Class Example:


{% highlight python %}

class DataSet:
    """A simple demonstration for adding an ITERATOR to a class."""

    def __init__(self, data=[]):
        self.data = data

    def __iter__(self):  # Set up the iterator cursor
        self.curr = 0
        return self

    def next(self):  # method called accessed in for loop.
        if self.curr >= len(self.data):
            raise StopIteration

        i = self.curr
        self.curr += 1
        return self.data[i]

if __name__ == '__main__':
    d = DataSet([2, 3, 5, 7, 8])
    for i in d:  # This is made possible because of __iter__ and next() functions in the DataSet class
        print i

{% endhighlight python %}



#### Binary Tree Sample Traversal

{% highlight python %}
"""
A BinaryTree class implemented with node/reference technique.

Illustrates 3 types of tree traversal.
"""

class BinaryTree:
    
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key),
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key),
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key),


if __name__ == '__main__':
    
    root = BinaryTree('g')
    root.insertLeft('u')
    root.insertRight('o')
    
    subtree_left = root.getLeftChild()
    subtree_left.insertLeft('i')
    subtree_left.insertRight('d')
    
    subtree_right = root.getRightChild()
    subtree_right.insertLeft('p')
    subtree_right.insertRight('y')

    #############################
    #             g             #
    #         ____|____         #
    #         u       o         #
    #       __|__   __|__       #
    #       i   d   p   y       #
    #############################

    print '\n Pre Order ==>\t ',
    root.preorder()
    print '\n  In Order ==>\t ',
    root.inorder()
    print '\nPost Order ==>\t ',
    root.postorder()
{% endhighlight python %}


---

{:.gray}
### 2017-04-10 Week 13

> [Homework 10 assigned](/345/hw10/)

### Trees

#### Readings
- **CHAPTER 8** ==> DSAP (Data Structures and Algorithms in Python)
- **Online Resource** ==> [Trees](http://interactivepython.org/runestone/static/pythonds/Trees/toctree.html)


#### Topics
- priority queues with min and max heaps
- binary trees

---

{:.gray}
### 2017-04-03 Week 12

> [Homework 9 assigned](/345/hw9/)

### Trees

#### Readings
- **CHAPTER 8** ==> DSAP (Data Structures and Algorithms in Python)
- **Online Resource** ==> [Trees](http://interactivepython.org/runestone/static/pythonds/Trees/toctree.html)

- [generators? lazy evaluation?](http://intermediatepythonista.com/python-generators)
- [more on generators](http://anandology.com/python-practice-book/iterators.html)

#### Topics
- tree data structure
- binary trees
- tree traversal

---

{:.gray}
### 2017-03-27 Week 11

### Midterm Results Review/Midterm Redux

---

{:.gray}
### 2017-03-13 Week 9

> Midterm Exam Wednesday 12:30-1:45

### Midterm Review Guide:
- HINT: review the homework assignment [homework list](/345/hw/) related to each topic below.
- HINT: *do the interactive exercises in the online chapter on algorithm analysis*

#### DSAP Chapter 1 basic python skills
- loops
- list comprehensions
- range function
- return statements
- branching
- exceptions
- functions (formal arguments, actual parameters)
- variable scope
- mutable and immutable data types
- pass by reference pass by value
- unit tests in python

#### DSAP Chapter 2 object oriented programming
- classes
	- definitions, 
	- object instantiation, 
	- class methods, 
	- constructors,
	- class attributes
	- Abstract Data Types

#### DSAP Chapter 4 recursion
- types (linear, binary, multiple, tail recursion)
	- **be able to recognize these types in code**
- understand the trace on p. 170 fig. 4.10
	- **be able to read and trace recursive code**

#### DSAP Chapter 6 stacks, queues, and deques
- understand the behavior of stacks and queues implemented as lists (arrays)
- understand the algorithm efficiency of these ADT's implemented as lists.

#### DSAP Chapter 7 linked lists
- understand the behavior of stacks and queues implemented as linked lists.
- understand the algorithm efficiency of stacks and queues implemented as linked lists.
- understand circular queues and related operations: rotate, enqueue, dequeue

#### Algorithm Analysis: Problem Solving with Algorithms... [pdf]({{ site.baseurl }}assets/cs345/ProblemSolvingwithAlgorithmsandDataStructures-chapter-2.pdf) [interactive](http://interactivepython.org/runestone/static/pythonds/index.html)
- understand the reason for doing algorithm analysis
- be able to perform algorithm analysis on short bits of code
- understand *O()* notation and the difference between the three that we discussed at length (1), (n), (n*n)
- pay attention to the discussion about efficiency of lists in python (e.g., pop() vs. pop(0))
- **Do the exercises**

---

{:.gray}
### 2017-03-06 Week 8

> [Homework 8 assigned](/345/hw8/)

### Algorithm Analysis 101

#### Readings
- **Chapter 2** ==> [Problem Solving with Algorithms...]({{ site.baseurl }}assets/cs345/ProblemSolvingwithAlgorithmsandDataStructures-chapter-2.pdf)
- **Online Version** ==> [Problem Solving with Algorithms Online...](http://interactivepython.org/runestone/static/pythonds/index.html)

#### Topics
- Algorithm analysis
- circular linked lists, circular arrays
- measuring performance

---


{:.gray}
### 2017-02-27 Week 7 

> [Homework 7 assigned](/345/hw7/)

### Recursion Review, Linked Lists

#### Readings
- **CHAPTER 4 and 7** ==> DSAP (Data Structures and Algorithms in Python)
- **Chapter 2** ==> [Problem Solving with Algorithms...]({{ site.baseurl }}assets/cs345/ProblemSolvingwithAlgorithmsandDataStructures-chapter-2.pdf)

#### Topics
- Recursion review
- Stack as linked list
- Queue as linked list
- Algorithm analysis Read ==> [Problem Solving with Algorithms...]({{ site.baseurl }}assets/cs345/ProblemSolvingwithAlgorithmsandDataStructures-chapter-2.pdf)
- **terms**: 

---

{:.gray}
### 2017-02-20 Week 6 

> [Homework 6 assigned](/345/hw6/)

### Recursion 

#### Readings
- **CHAPTER 4** ==> DSAP (Data Structures and Algorithms in Python)

#### Topics
- designing recursive algorithms
	- identify smallest problem
	- identify **base case**
	- identify **recursive case**
- recursive binary search
- a simple linked list
- **terms**: ```activation record (stack frame)```, ```base case```, ```recursive case```, ```linear, binary, multiple recursion```, ```tail recursion```

---

{:.gray}
### 2017-02-13 Week 5 

> [Homework 5 assigned](/345/hw5/)

### Data File Handling/Recursion 

#### Readings
- **CHAPTER 4** ==> DSAP (Data Structures and Algorithms in Python)

#### Topics
- REVIEW: file reading and basic data processing with objects and json
- serialization and deserialization techniques
- file/directory organization
- recursion
- [generators? lazy evaluation?](http://intermediatepythonista.com/python-generators)

---

{:.gray}
### 2017-02-06 Week 4 

> [Homework 4 assigned](/345/hw4/)

### Object Oriented Programming with Python

#### Readings
- **CHAPTER 1 & 2** ==> DSAP (Data Structures and Algorithms in Python)

#### Topics
- classes and objects in python
- object oriented design
- file reading and basic data processing with objects and json

---

{:.gray}
### 2017-01-30 Week 3 

> [Homework 3 assigned](/345/hw3/)

### Python Primer Cont. and Object Oriented Programming

#### Readings
- **CHAPTER 1 & 2** ==> DSAP (Data Structures and Algorithms in Python)

#### Topics
- dictionaries, sets, and lists
- exceptions ==> *ask for forgiveness not permission*
- raising exceptions
- classes and objects in python

---

{:.gray}
### 2017-01-23 Week 2 

#### Readings
- **CHAPTER 1** ==> DSAP (Data Structures and Algorithms in Python)

##### Additional reference:
[python scope and namespace](http://www.python-course.eu/passing_arguments.php)

[python data structures](https://docs.python.org/2/tutorial/datastructures.html#)

#### Topics
- Python primer (variables, conditionals, iteration)
- mutability/immutability
- scope and namespace
- pass by value vs. pass by reference 
- review homework 1

#### Note on ```mutability/immutability``` and ```pass-by-value/pass-by-reference```.

> FACT 1: Python passes all arguments by reference.

> FACT 2: Data types in python are either ```mutable``` or ```immutable```.

##### GIVES THE FOLLOWING CONCLUSIONS:
> If an **immutable** type is passed as an argument to a function, it is passed by reference. However, because the argument is **immutable** it cannot be reassigned a value. Thus, any modification to the argument is necessarily a **COPY**. This effectively indicates that **immutable** types are **passed by value**.

> If a **mutable** type is passed as an argument to a function, it is passed by reference. Therefore, it can be modified directly. This follows the behavior consistent with what we mean by **pass-by-reference**.


---

{:.gray}
### 2017-01-18 Week 1 

#### Readings
- DSAP (Data Structures and Algorithms in Python) ==> CHAPTER 1

#### Topics
- course introduction and overview
- Python primer 1 (variables, conditionals, iteration)

---

{% comment %}

### 2017-01-18 Week 1 ### Introduction
### 2017-01-23 Week 2 ### Python Primer
### 2017-01-30 Week 3 ### Python Primer Cont. and Object Oriented Programming
### 2017-02-06 Week 4 ### Object Oriented Programming with Python
### 2017-02-13 Week 5 ### Data File Handling/Recursion 
### 2017-02-20 Week 6 ### Algorithm Analyis
### 2017-02-27 Week 7 ### TBD
### 2017-03-06 Week 8 ### TBD
### 2017-03-13 Week 9 ### Midterm
### 2017-03-20 Week 10 ### Spring Break
### 2017-03-27 Week 11 ### TBD
### 2017-04-03 Week 12 ### TBD
### 2017-04-10 Week 13 ### TBD
### 2017-04-17 Week 14 ### TBD
### 2017-04-24 Week 15 ### TBD
### 2017-05-01 Week 16 ### TBD
### 2017-05-08 Week 17 ### Final Exam Week

{% endcomment %}

