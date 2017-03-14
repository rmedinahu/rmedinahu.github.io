---
layout: course_page
title: schedule
permalink: /431/schedule/
parent_course: 431
---

**Spring 2017 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6), [7](#week-7), [8](#week-8)

---
{:.green}
### 2017-03-13 Week 9

> Midterm Exam Wednesday 11:00-12:15

### Midterm Review
- HINT: *review the homework assignment solutions*
- HINT: *below are links to the relevant ppt slides for each chapter, review*

#### DBI Chapter 3
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
- *be able to read an E-R diagram and make interpretations about its structure*

#### DBI Chapter 4
- Relational Algebra Operators (and examples of applying these operators to sample relations):
	- SELECT
	- PROJECT
	- BINARY PRODUCT
	- THETA JOIN / EQUIJOIN / NATURAL JOIN

#### DBI Chapter 5
- choosing a primary key
- SQL DDL (be able to recognize sql data definition commands from E-R diagrams)
	- create table
	- constraints (not null, primary key, foreign key)

- SQL DML (be able to read sql statements and deduce results)
	- select/project/predicate
	- join two tables
	- join three tables
	- WHERE, ORDER BY statements

---

{:.gray}
### 2017-03-06 Week 8

> [homework 6 assigned](/431/hw6/)

### Constructing and Using a Relational DB 

#### Readings
- **Chapter 5** ==> (DBI) Databases Illuminated
- **POWERPOINT SLIDES** ==> [[Chapter 5]]({{ site.baseurl }}assets/cs431/9781284079050_SLID_CH05.ppt)

#### Topics
- working with sql

---

{:.gray}
### 2017-02-27 Week 7 

> [homework 5 assigned](/431/hw5/)

### Constructing and Using a Relational DB 

#### Readings
- **Chapter 5** ==> (DBI) Databases Illuminated
- **POWERPOINT SLIDES** ==> [[Chapter 5]]({{ site.baseurl }}assets/cs431/9781284079050_SLID_CH05.ppt)
- [relationa_model_operations.py]({{ site.baseurl }}assets/cs431/relationa_model_operations.py)

#### Topics
- E-R to db tables
- relational operators (theory) ```SET, PROJECT, JOIN (theta, equijoin, natural, left, right, outer)
- SQL as DDL and DML- **Case Study:** A simple cars database

#### CARS: Super Simple Relational DB

A. Use sqlite3 to create a db:

``` sqlite3 car_db.db```

B. Load the tables from external sql file [cars.sql]({{ site.baseurl }}assets/cs431/cars-demo/cars.sql)

```sqlite3> .read cars.sql```

C. Load data from csv *fixtures* [cars.csv]({{ site.baseurl }}assets/cs431/cars-demo/cars.csv) and [makes.csv]({{ site.baseurl }}assets/cs431/cars-demo/makes.csv)

```sqlite3> .separator ","```

```sqlite3> .import makes.csv makes```

```sqlite3> .import cars.csv cars```

#### Now you can try running these queries in the sqlite3 shell.

{% highlight sql %}
/* Sample sql statements for the cars demo db. Setup the DB before running these.*/

/*SELECT (single table)*/
select * from cars;

/*SELECT THEN PROJECT (single table)*/
select cars.year, cars.odom from cars;

/*BINARY PRODUCT JOIN (cartesian product)*/
select * from cars inner join makes;

/*THETA JOIN (product then select)*/
select makes.make, cars.year from cars inner join makes;

/*EQUI JOIN or NATURAL JOIN (product then select predicate on col in A == col in B) */
select cars.year, makes.make from cars inner join makes on makes.pk = cars.make;
{% endhighlight sql %}


---

{:.gray}
### 2017-02-20 Week 6 

### Relational Model

#### Readings
- **Chapter 4 & 5** ==> (DBI) Databases Illuminated
- **POWERPOINT SLIDES** ==> [[Chapter 4]]({{ site.baseurl }}assets/cs431/9781284079050_SLID_CH04.ppt)

#### Topics
- db modeling review
- case study: Design a db for a multiple choice test.

> A online testing app displays multiple choice tests. All tests must contain 20 multiple choice questions. Each question contains up to 5 possible choices. The testing app allows any number of students to take any number of tests. The test score for each student must be recorded for eternity.

- what to indicate:
	- entities and relations
	- cardinalities and participation constraints using (min, max)
- relational model
	- database correctness?
	- relations and tables
	- keys
	- schemas (DML, DDL)
- playing with the relational model:

{% highlight python %}

import itertools

# roll your own ascii character generator.
alpha = [chr(i) for i in range(65, 65+26)] + [chr(i) for i in range(97, 97+26)] + [chr(i) for i in range(48, 58)]

##### Schema Example ==> (attr1, attr2, attr3)

# generate the cartesian product of sets of ascii characters (D1 * D2 * D3)
sets = list(itertools.product(alpha, alpha, alpha))

# a "relation" is a subset of sets:
rel = [i for i in sets if i[0] == 'A' and i[2] == 'Z']

##### Another Schema Example ==> (make, year, odometer)
domain_make = ['ford', 'dodge', 'gmc', 'chevy']
domain_year = range(2000, 2018)
domain_odom = range(50000, 200000, 50000)

# generate the cartesian product of sets of ascii characters (D1 * D2 * D3)
sets = list(itertools.product(domain_make, domain_year, domain_odom))

# a "relation" is a subset of sets:
rel = [i for i in sets if i[0] == 'ford' and i[2] == 2017]

{% endhighlight python %}


---

{:.gray}
### 2017-02-13 Week 5 

### Database Design/Relational Model: EE-R Modeling

#### Readings
- **Chapter 3 & 4** ==> (DBI) Databases Illuminated
- **POWERPOINT SLIDES** ==> [[Chapter 3]]({{ site.baseurl }}assets/cs431/9781284079050_SLID_CH03.ppt) [[Chapter 4]]({{ site.baseurl }}assets/cs431/9781284079050_SLID_CH04.ppt)

#### Topics
- Extended E-R (EE-R) modeling
- generalization
- specialization
	- total/partial
	- disjoint/overlapping
	- predicate defined (attribute or user defined)
- union
	- total/partial category
- relational model
- case study: a *non*-relational database
	- [data.txt]({{ site.baseurl }}assets/cs345/data.txt)
	

---

{:.gray}
### 2017-02-06 Week 4 

### Database Design: E-R and EE-R Diagrams

> [homework 4 assigned](/431/hw4/)

#### Readings
- **Chapter 3** ==> (DBI) Databases Illuminated
- **POWERPOINT SLIDES** ==> [Chapter 3]({{ site.baseurl }}assets/cs431/9781284079050_SLID_CH03.ppt)

#### Topics
- E-R (Entity-Relationship) Model (entities, attributes, relations)
- *Relationship degree*: ```unary```, ```binary```, ```ternary```, ```n-ary```
- *Binary relationships*: ```cardinality```
	* one-to-one, one-to-many, many-to-one, many-to-many
- *Participation*: min, max
- *weak/strong entities*
- EE-R diagrams
- generalization/specialization
- unions
- case study: a DB for a small motel in Wagon Mound NM:
	- entities, attributes, relations?
	- queries?

---

{:.gray}
### 2017-01-30 Week 3 

> [homework 3 assigned](/431/hw3/)

### Database Architecture Foundations and Design

#### Readings
- **Chapter 2 & 3** ==> (DBI) Databases Illuminated

#### Topics
- review of DBMS software
- DB architecture: layers and stages
- DB design
- a look at application level design: *The case of the overworked manager*
- E-R (Entity-Relationship) Model (entities, attributes, relations)

---

{:.gray}
### 2017-01-23 Week 2 

> [homework 2 assigned](/431/hw2/)

#### Readings
- **Chapter 1** ==> (DBI) Databases Illuminated

#### Topics
- *relational db overview
- *rdb application stack
- tour of rdb driven web application
- overview of db management software
- a look at LibreOffice Base

---

{:.gray}
### 2017-01-18 Week 1 

> [homework 1 assigned](/431/hw1/)


#### Readings
- interwebs

#### Topics
- course introduction and overview
- the data-driven application stack
- db tour of data driven web application

---

{% comment %}
### 2017-01-18 Week 1 ### Introduction
### 2017-01-23 Week 2 ### Relational DB/Applications
### 2017-01-30 Week 3 ### Database Architecture Foundations and Design
### 2017-02-06 Week 4 ### Database Design: E-R and EE-R Diagrams
### 2017-02-13 Week 5 ### Database Design/Relational Model: EE-R Modeling
### 2017-02-20 Week 6 ### Relational Model
### 2017-02-27 Week 7 ### Relational Model
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

