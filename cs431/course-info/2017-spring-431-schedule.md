---
layout: course_page
title: schedule
permalink: /431/schedule/
parent_course: 431
---

**Spring 2017 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6), [7](#week-7), [8](#week-8), [9](#week-9), [11](#week-11), [12](#week-12), [13](#week-13), [14](#week-14), [15](#week-15)

---

{:id="week-15" .green}
## 2017-04-24 Week 15

### Application Programming Interfaces/Database Normalization

> ["Homework" 8 Normalization Self Study]({{ site.baseurl }}assets/cs431/normalization-study.pdf) (not to be turned in)

#### Readings
- **Chapter 6** ==> (DBI) Databases Illuminated
- **POWERPOINT SLIDES** ==> [[Chapter 6]]({{ site.baseurl }}assets/cs431/9781284079050_SLID_CH06.ppt)
- [Shorter Overview of DB Normalization]({{ site.baseurl }}assets/cs431/stephens-database-design-ch06-2015.pdf)
- [db rankings](https://db-engines.com/en/ranking)

#### Topics
- application layer programming interfaces
	- ```psycopg2``` (python api for ```postgresql```)
	- ```mysql connector``` (python api for ```mysql```)
	- Django programming api: ```querysets```
- database design - normalization
	- normalization: flexibility, extendibility, integrity constraints, reduce redundancy, storage and inconsistencies
	- *anamolies* (insertion, update, deletion) lead to inconsistent databases
	- *dependencies* (functional, multivalued, join)
	- superkey -> candidate key -> primary key
- 1NF - no multivalued attributes
- 2NF - full functional dependency on primary key
- 3NF - no transitive dependencies exist
- BCNF - x --> a then x IS superkey (more strict)

#### Case Study: API examples in Mysql and Postgresql
- [mysql python connector](https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html)
- [mysql connector example](https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html)

{% highlight python %}
import mysql.connector

cnx = mysql.connector.connect(user='username', password='password', database='dbname')

cursor = cnx.cursor()
query = ("select * from users;")
cursor.execute(query)

# cursor contains an iterator of results
for i in cursor:
    print i
{% endhighlight python %}

- [psycopg2 connector](http://initd.org/psycopg/docs/)
- [psycopg2 example](http://initd.org/psycopg/docs/usage.html)
- [Django DB API](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#queryset-api-reference)
	- api is abstracted away from specific db
	- api supports at least: sqlite, mysql, postgresql, oracle


---

{:id="week-14" .gray}
## 2017-04-17 Week 14

### SQL and Database Normalization

#### Readings
- **Chapter 6** ==> (DBI) Databases Illuminated


#### Topics
- outer joins
- database design - normalization
- MySQL 

#### Case Study: Outer Joins
- SQL to build and populate a small database: [enroll-analytics-small.sql]({{ site.baseurl }}assets/cs431/enroll-analytics-small.sql)

- Example queries using outer joins **(updated after corrections at 3:15pm apr 17)**:

{% highlight sql %}
-- enrollment analytics small 

-- a simple natural join of schedules and courses
create or replace view natural_join_view as
    select schedules.semester_pk as semester_schedule, courses.title as course
    from schedules left join courses
    on schedules.course_pk = courses.pk;

-- a left outer join (keep the left table rows and show unmatched rows in right table)
-- shows all semesters that do not have scheduled classes...ever. Should NOT have nulls
-- because there are no unmatched semester pks in the schedule table (all 10 schedule records
-- are associated with a semester record).
create or replace view left_outer_view as
    select schedules.semester_pk as semester_schedule, semesters.title as semester
    from schedules left outer join semesters
    on schedules.semester_pk = semesters.pk;

-- a right outer join (keep the right table rows and show unmatched rows in left table)
-- shows all semesters that have AND do not have an association with schedule table. Should
-- show those semesters that don't have a matching reference in the schedule table (they are null)
-- as well as those that DO HAVE a matching reference.
create or replace view right_outer_view as
    select schedules.semester_pk as semester_schedule, semesters.title as semester
    from schedules right outer join semesters
    on schedules.semester_pk = semesters.pk
    order by semester_schedule;


-- a right outer join (keep the right table rows and show unmatched rows in left table)
-- shows which courses that have and do not have a reference from the schedule table. 
-- Indicates which courses that do not appear in the schedule table
create or replace view untaught_courses_view as
    select schedules.course_pk as scheduled_course, courses.title
    from schedules right outer join courses
    on schedules.course_pk = courses.pk;
{% endhighlight sql %}

---

{:id="week-13" .gray}
## 2017-04-10 Week 13

### SQL w/MySQL

#### Readings
- **Chapter 5** ==> (DBI) Databases Illuminated


#### Topics
- Advanced queries: nested select, aggregation, views, functions
- MySQL 

---

{:id="week-12" .gray}
## 2017-04-03 Week 12

> [homework 7 assigned](/431/hw7/)


### SQL w/MySQL

#### Readings
- **Chapter 5** ==> (DBI) Databases Illuminated

- [MySQL Docs](https://dev.mysql.com/doc/refman/5.7/en/)
- [MySQL sql functions](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [MySQL shell commands](https://dev.mysql.com/doc/refman/5.7/en/mysql-batch-commands.html)
- [MySQL external import](https://dev.mysql.com/doc/refman/5.7/en/mysqlimport.html)


#### Topics
- Advanced queries: nested select, aggregation, views, functions
- MySQL 


#### Case Study: MySQL Tracking User Logins

[tracked_users_data.sql]({{ site.baseurl }}assets/cs431/tracked_users_data.sql)

#### Sample SQL using nested queries and views:
**using db in [enroll-db-demo.zip]({{ site.baseurl }}assets/cs431/enroll-db-demo.zip)**

{% highlight sql %}
drop view course_history_view;
drop view enroll_avg_view;

-- groups courses by semester then title, shows total enrollment of aggregation
select sum(schedules.actual_enroll) as enroll_count, semesters.title, semesters.code as sem, courses.level, courses.title as crs_title
from schedules, courses, semesters
on schedules.course_pk = courses.pk and schedules.semester_pk = semesters.pk
-- where courses.title like "%machine learning%"
group by semesters.code, courses.title
order by semesters.code;

-- above query as a view
create view if not exists course_history_view as
    select sum(schedules.actual_enroll) as enroll_count, semesters.title, semesters.code as sem, courses.level, courses.title as crs_title
    from schedules, courses, semesters
    on schedules.course_pk = courses.pk and schedules.semester_pk = semesters.pk
    -- where courses.title like "%machine learning%"
    group by semesters.code, courses.title
    order by semesters.code;

-- calculates average enrollment by course in entire db
create view if not exists enroll_avg_view as
    select avg(enroll_count) as a, crs_title
    from course_history_view
    group by crs_title
    order by a;
{% endhighlight sql %}


---

{:id="week-11" .gray}
## 2017-03-27 Week 11

### SQL

#### Readings
- **Chapter 5** ==> (DBI) Databases Illuminated

#### Topics
- Advanced queries: nested select, aggregation, views

[enroll-db-demo.zip]({{ site.baseurl }}assets/cs431/enroll-db-demo.zip)

---

{:id="week-9" .gray}
## 2017-03-13 Week 9

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

{:id="week-8" .gray}
## 2017-03-06 Week 8

> [homework 6 assigned](/431/hw6/)

### Constructing and Using a Relational DB 

#### Readings
- **Chapter 5** ==> (DBI) Databases Illuminated
- **POWERPOINT SLIDES** ==> [[Chapter 5]]({{ site.baseurl }}assets/cs431/9781284079050_SLID_CH05.ppt)

#### Topics
- working with sql

---

{:id="week-7" .gray}
## 2017-02-27 Week 7 

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

{:id="week-6" .gray}
## 2017-02-20 Week 6 

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

{:id="week-5" .gray}
## 2017-02-13 Week 5 

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

{:id="week-4" .gray}
## 2017-02-06 Week 4 

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

{:id="week-3" .gray}
## 2017-01-30 Week 3 

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

{:id="week-2" .gray}
## 2017-01-23 Week 2 

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

{:id="week-1" .gray}
## 2017-01-18 Week 1 

> [homework 1 assigned](/431/hw1/)


#### Readings
- interwebs

#### Topics
- course introduction and overview
- the data-driven application stack
- db tour of data driven web application

---

{% comment %}
## 2017-01-18 Week 1 ### Introduction
## 2017-01-23 Week 2 ### Relational DB/Applications
## 2017-01-30 Week 3 ### Database Architecture Foundations and Design
## 2017-02-06 Week 4 ### Database Design: E-R and EE-R Diagrams
## 2017-02-13 Week 5 ### Database Design/Relational Model: EE-R Modeling
## 2017-02-20 Week 6 ### Relational Model
## 2017-02-27 Week 7 ### Relational Model
## 2017-03-06 Week 8 ### TBD
## 2017-03-13 Week 9 ### Midterm
## 2017-03-20 Week 10 ### Spring Break
## 2017-03-27 Week 11 ### TBD
## 2017-04-03 Week 12 ### TBD
## 2017-04-10 Week 13 ### TBD
## 2017-04-17 Week 14 ### TBD
## 2017-04-24 Week 15 ### TBD
## 2017-05-01 Week 16 ### TBD
## 2017-05-08 Week 17 ### Final Exam Week

{% endcomment %}

