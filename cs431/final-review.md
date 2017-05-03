---
layout: course_page
title: Final Exam Review
permalink: /431/final-review/
parent_course: 431
---

## Final Review

- Exam will consist of no more than 25 multiple choice questions. I will reuse some questions from the midterm exam. Be sure to study the midterm in D2L. You should still have access to the midterm. Each question includes your response and the correct answer.

> (1) Choose quizzes from Assessment menu, (2) find midterm exam in list, (3) select attempts from menu attached to quiz title. 

- HINT: *review the homework assignment solutions. Be very familiar with how hw7 solution works.*
- HINT: *below are links to the relevant ppt slides for each chapter to review*

#### DBI Chapter 3
*Be able to read an E-R diagram and make interpretations about its structure*

- E-R diagrams
- entities, attributes, primary keys **3.3**, **3.4**
- relationships **3.5**
	- cardinality
	- attributes
	- participation constraints.
	- *(min, max)* ==> cardinality and participation
- EE-R diagrams
	- specialization/generalization
	- why was E-R extended to EE-R?
- strong vs. weak entities

#### DBI Chapter 4
- Relational Algebra Operators (and examples of applying these operators to sample relations):
	- SELECT
	- PROJECT
	- BINARY PRODUCT
	- NATURAL JOIN

#### DBI Chapter 5
- SQL DDL (be able to recognize relevant sql data definition commands from E-R diagrams)
	- create table
	- constraints (not null, primary key, foreign key)

- SQL DML (be able to read sql statements and deduce results)
	- select/project/predicate
	- join two tables
	- join three tables
	- WHERE, ORDER BY statements

*New since midterm:*

- SQL Nested Queries
	- be able to read and understand nested select queries. [HW7](/431/hw7/) solution provides examples.
- SQL Views
	- be able to read and understand views and how they are used. [HW7](/431/hw7/) solution provides examples.
- Foreign key concepts:
	- home relation
	- ON DELETE CASCADE
	- ON DELETE SET NULL
	- ON DELETE PROTECT

#### DBI Chapter 6
- Resources:
	- [Stephens' normalization example]({{ site.baseurl }}assets/cs431/stephens-database-design-ch06-2015.pdf)
	- [normalization example]({{ site.baseurl }}assets/cs431/normalization-study.pdf)
- DB Normalization:
	- why and when? (to eliminate anamolies, normalization conducted during design)
	- be able to recognize and provide examples of ```insert```, ```update```, and ```delete``` anamolies
- Normal Forms
	- be able to assess whether a table is in ```1NF```, ```2NF```, or ```3NF```
	- be able to identify actions to put a table in ```1NF```, ```2NF```, or ```3NF``` 

#### Graduate Presentations:
- Using the linked grad presentations, be able to answer the following.
- What is DBaas? [ben]({{ site.baseurl }}assets/cs431/benji-dbaas.pdf)
- How do nosql and rdbms systems (oracle) differ in how they store data? [lavanya]({{ site.baseurl }}assets/cs431/lavanya-nosql-rdbs.pdf)





