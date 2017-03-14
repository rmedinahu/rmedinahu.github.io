---
layout: course_page
title: schedule
permalink: /451/schedule/
parent_course: 451
---

**Spring 2017 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6), [7](#week-7), [8](#week-8)

---
{:.green}
### 2017-03-13 Week 9

> Midterm Exam Thursday 11 - 12:15

### Midterm Review Guide:

- HINT: review the weekly schedule for details and (mainly) chapter 3 and 4 of textbook

#### Git
- repository: working copy, remote copy
- branches
- forks
- procedures for collaboration (pull and push)
- conflict resolution (in code!)

#### Testing
- pytest vs. unittest vs. doctest

#### Application Development
- requirements files
- project layouts
- virtual environments
- pip
- understand philosophy of *release early release often*
- why are prime directives critical to success of open source software?
- the overarching message in Cathedral and the Bazaar?
- bugs (finding them or fixing them. which is more difficult?)

#### Documentation
- pydoc

#### Project Management (chapter 3)
- pert (program evaluation and review technique) / gantt charts
- CPM: critical path methods

#### Requirements/Design (chapter 4)
- purpose of requirements and categories
- use cases 

---

{:.gray}
### 2017-03-07 Week 8 

### Requirements

#### Readings
- **Chapter 4** ==> BSE

#### Topics
- requirements gathering
	- clear
	- unambiguous
	- consistent
	- verifiable
	- prioritized (must, should, could, won't = MOSCOW method)
- types of requirements (lists and narratives)
- FURPS+ (but see textbook template for requirements categories below.)
- graduate students ==> project planning
- **case study**: Gathering Requirements in Teams

*For this case study, each person listed under their respective assigned projects below will gather together and devise a list of requirements for the project. The project manager/grad student will lead these discussions. Once requirements are agreed upon, the PM will post these requirements to the requirements document on their respective GitHub repository site (the "wiki"). We will review these requirements as a class.*

##### Team: Message in a Bottle [message-bottle-py](https://github.com/rmedinahu/message-bottle-py)
*Project Manager*: LG

*Project Team*: MA, TH, NN, AM

[requirements doc](https://github.com/rmedinahu/message-bottle-py/wiki/Requirements)
       
##### Team: Link Smark [link-smark-py](https://github.com/rmedinahu/link-smark-py)
*Project Manager*: RV

*Project Team*: FS, HC, JI

[requirements doc](https://github.com/rmedinahu/link-smark-py/wiki/Requirements)

##### Team: Book Flea [book-flea-py](https://github.com/rmedinahu/book-flea-py)
*Project Manager*: SG

*Project Team*: JM, MR, SE, NH

[requirements doc](https://github.com/rmedinahu/book-flea-py/wiki/Requirements)

#### Bare Bones Requirements Template

	TITLE:

	OVERVIEW/DESCRIPTION

	BUSINESS REQUIREMENTS

	USER REQUIREMENTS

	FUNCTIONAL REQUIREMENTS

	NONFUNCTIONAL REQUIREMENTS

	IMPLEMENTATION REQUIREMENTS

	USE CASES:


#### FURPS+ Requirements Template (functionality, usability, reliability, performance, scalability)

	TITLE:

	OVERVIEW/DESCRIPTION

	FUNCTIONAL REQUIREMENTS (what the program should do?)

	USABILITY REQUIREMENTS (what the program should look like?)

	RELIABILITY REQUIREMENTS (how reliable the system should be?)

	PERFORMANCE REQUIREMENTS (how efficient should the system be?)

	SUPPORTABILITY REQUIREMENTS (how easy should the system be to support?)

	DESIGN REQUIREMENTS (design constraints?)

	IMPLEMENTATION REQUIREMENTS (contraints on the way the software is built)

	INTERFACE REQUIREMENTS (interfaces with other systems?)

	PHYSICAL REQUIREMENTS (hardware requirements?)


	USE CASES:

---

{:.gray}
### 2017-02-28 Week 7 

### Frameworks & Project Management

#### Readings
- **Chapter 3** ==> BSE

#### Topics
- bug/issue tracking Github **issues**
- team management
- task management
- modularity
- graduate students ==> project planning meeting

---

{:.gray}
### 2017-02-21 Week 6 

### Frameworks & Project Management

#### Readings
- **Chapter 3** ==> BSE

#### Topics
- testing and documentation review
- application frameworking
- project management
- software dev skill: ```issues``` with GitHub

#### software dev skill: ```pyramid``` basic intro
- [Pyramid Web Application Framework](https://trypyramid.com/)
- [Pyramid Installation (Hey! There's Documentation!?!)](http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html)
- [Pyramid Basic Ops: Hello World Tutorial](http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/firstapp.html)

#### software dev skill: ```pyramid``` == NOT starting from scratch == [Pyramid Cookiecutter Tutorial](http://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/cookiecutters.html)

##### Developing on a Framework
1. Once you have the cookiecutter project running __AND VISIBLE IN A BROWSER__ ...
2. Come up with a **randomly** interesting *nickname* for your project. See the function below for ideas. You will need to add this function to your views then use it to generate a random nickname. Add this nickname as *new* variable to your view then modify the relevant template file in your project (```templates/mytemplate.jinja2```). Test in a browser.

{:.yellow}
> NOTE: you may encounter *not found* errors during the testing phase below. Study these and run the appropriate ```pip install``` commands to get them fixed.

##### Testing on a Framework
3. Now modify ```test.py``` to test the value of your *nickname* variable. See function: ```test_my_view(request). ``` Run pytest  ```py.test``` from the project root folder.
4. There's a random chance that your tests will pass but you get the idea! *Why is there a random chance tests will pass?* :)
4. After your testing, initialize your project with git (**make sure you are in the project root!**)
5. Create a git repo on GitHub then add it as a remote to your pyramid project (initialized in the previous step right?).


{% highlight python %}
import random

def get_random_nickname():
    adjvs = ['golden', 'ruby', 'fuzzy', 'liquid', 'sour', 'snowy', 'blazing']
    nouns = ['shores', 'keys', 'peaks', 'smiles', 'jungles', 'skies', 'forests']

    return random.choice(adjvs) + ' ' + random.choice(nouns)

{% endhighlight python %}


---

{:.gray}
### 2017-02-14 Week 5 

> [Homework 4 assigned](/451/hw4)

> [Homework 3 assigned](/451/hw3)

### Basic Documentation/Testing

#### Readings
- **Chapter 2 & 3** ==> BSE

#### Topics
- software dev skill: git ```fork``` and git ```branch```
- unit testing : **unittest**, **pytest**, **doctest**

- software dev skill: ```unittest``` module
	1. create python file for your test cases. ```test_mystuff.py```
	2. run the unit tests in your test file. ```python test_mystuff.py```
	3. cross your fingers...

- software dev skill: ```pytest``` module
	0. install pytest if needed: ```pip install pytest```
	1. assume you have a source file: ```sample.py```
	2. create python file for your test cases. ```test_sample.py``` (prepending with test allows pytest to find your test cases!)
	3. add unit tests to your test file.
	4. run your unit tests from project root or in src dir: ```py.test```

- Example:

	{% highlight python %}
	# sample.py
	# Using unit tests included in docstrings 
	# See test_sample.py for unit tests that utilize pytest

	def pow_of_two(x):
	    """Return x to the power of 2.

	    >>> pow_of_two(2)
	    4
	    >>> pow_of_two(-2)
	    4
	    """
	    return x**2

	def float_div_by_two(x):
	    """Return x divided by 2 in floating point precision.

	    >>> float_div_by_two(49)
	    24.5
	    >>> float_div_by_two(48)
	    24.0
	    """
	    return x / 2.0

	if __name__ == '__main__':
	    import doctest
	    doctest.testmod()
	{% endhighlight python %}

---

	{% highlight python %}
	# test_sample.py
	# Demonstrates unit testing using the pytest module.
	# pytest must be installed through pip.

	from sample import pow_of_two, float_div_by_two

	def test_pow_of_two():
	    assert pow_of_two(3) == 9

	def test_float_div_by_two():
	    assert float_div_by_two(5) == 2.5
	{% endhighlight python %}


- documentation (developer/user): **pydoc**

- software dev skill: ```pydoc``` module
	1. add documentation to your source code and save. ```sample.py```
	2. in shell, run ```pydoc -w ./sample.py``` to generate a documentation page in html. Should be ```sample.html```
	3. take a look at your fine work in a browser.

#### Python Tools
- [about git fork](https://help.github.com/articles/fork-a-repo/)

- documentation generators
	- [pydoc](https://docs.python.org/2/library/pydoc.html)
	- [doctest](https://docs.python.org/2.7/library/doctest.html?highlight=doctest#module-doctest)

- unit testing tools
	- [Python unittest module (builtin)](https://docs.python.org/3/library/unittest.html)
	- [pytest](http://docs.pytest.org/en/latest/)
	- [Hitchhiker's Guide to Writing Tests](http://docs.python-guide.org/en/latest/writing/tests/)

---

{:.gray}
### 2017-02-07 Week 4 

> [Homework 2 assigned](/451/hw2)

### Overview of Modern Software Development Components

#### Readings
- **Chapter 2 & 3** ==> BSE

#### Topics
- prime directives
- introduction of model-view-controller design pattern
- software dev skill: virtual environments and projects
- software dev skill: requirements file
- software dev skill: creating a project shell

#### Prime Directives for Open Source Software Development
developed by Philip Johnson, University of Hawaii 
 
*While Open Source licensing creates a legal mechanism for developers to collaboratively develop software
source code and distribute it, there are many software projects that fail to function as an open source
project—in other words, they fail to attract users, and they fail to attract developers.*   

*The three Prime Directives for Open Source Software Engineering provide a simple means to assess whether or not a software project has the potential to successfully function in the open source community. Satisfying the three prime directives does not guarantee that an open source community will grow up around the project, but failure to satisfy them will make it significantly more difficult for such a community to emerge.* 
 
**1. THE SYSTEM SUCCESSFULLY ACCOMPLISHES A USEFUL TASK.** 

> The system does not have to include every bell and whistle to accomplish a useful task. Indeed, the art of incremental development is to determine the smallest useful increment of functionality and implement
that first. In most cases, careful thought, ample user interaction, and efficient design and implementation can lead to a first public release with some useful functionality within weeks after project inception. A system developer cannot verify that the system achieves PD #1. Only an external user can. 
 
**2. AN EXTERNAL USER CAN SUCCESSFULLY INSTALL AND USE THE SYSTEM.** 

> The system must include sufficient user-level documentation to support download, installation, and use of
the system without significant interaction with a system developer. Typically, but not always, the system must also be distributed in an executable form so that external users do not have to compile the system themselves. A system developer cannot verify that the system achieves PD #2. Only an external user can. 
 
**3. AN EXTERNAL DEVELOPER CAN SUCCESSFULLY UNDERSTAND AND ENHANCE THE SYSTEM.** 

> The system must include developer-level documentation providing insights into the design and
development of the system that enable an external developer to understand and enhance it.


---

{:.gray}
### 2017-01-31 Week 3 

### Modern Software Development/Git Preliminaries

> [Homework 1 assigned](/451/hw1)

#### Readings

- **Chapter 1** ==> Beginning Software Engineering (BSE)

#### Topics
- * modules and frameworks
- * software engineering and complexity
	- a walk through a somewhat complex software project
- * git preliminaries
- * git in depth
- * github pages

#### Git Exercise

1. In pairs, choose a team leader and a team member.

2. Team leader creates a gitub project containing a single file with the code listed below.

3. Team leader pushes the file from [2] as first commit to github. Team leader adds team member as collaborator and shares the github link to the project in [2] with team member.

4. Team member clones the project in [2] and begins work on the indicated function.

5. Team leader begins work on the indicated function.

6. Leader and member write, test, and debug their respective code. When their portion is complete, they commit and push their changes to github.

7. Each member should then pull changes to THEIR working copy to see the "merge" of each respective code segment.

{% highlight python %}
# git-exercise-01.py

# TEAM LEADER:
# implement this function so that it returns copy of string_arg reversed
def reverseWord(string_arg):
	pass

# TEAM MEMBER:
# implement this function so that it returns the frequency of query in string_arg
def countFreq(string_arg, query):
	pass

def main():
	data = 'guidorossumwashere'
	print 'REVERSED ==>', reverseWord(data)
	print 'FREQUENCY OF s IN', data, '==>', countFreq(data, 's')

if __name__ == "__main__": 
	main()

{% endhighlight python %}

---

{:.gray}
### 2017-01-24 Week 2 

### Philosophy of Open Source Software Development

#### Readings
[cathedral-bazaar.pdf]({{ site.baseurl }}assets/cs451/cathedral-bazaar.pdf)

#### Topics
- discussion of Cathedral and the Bazaar reading
- lessons from the open source software philosophy



#### CATB Principles:

1. Every good work of software starts by scratching a developer’s personal itch.
2. Good programmers know what to write. Great ones know what to rewrite (and reuse).
3. “Plan to throw one away; you will, anyhow.” (Fred Brooks, The Mythical Man-Month, Chapter 11)
4. If you have the right attitude, interesting problems will find you.
5. When you lose interest in a program, your last duty to it is to hand it off to a competent successor.
6. Treating your users as co-developers is your least-hassle route to rapid code improvement and effective debugging.
7. Release early. Release often. And listen to your customers.
8. Given a large enough beta-tester and co-developer base, almost every problem will be characterized quickly and the fix obvious to someone.
9. Smart data structures and dumb code works a lot better than the other way around.
10. If you treat your beta-testers as if they’re your valuable resource, they will respond by becoming your most valuable resource.
11. The next best thing to having good ideas is recognizing good ideas from your users. Sometimes the latter is better.
12. Often, the most striking and innovative solutions come from realizing that your concept of the problem was wrong.
13. “Perfection (in design) is achieved not when there is nothing more to add, but rather when there is nothing more to take away.”
14. Any tool should be useful in the expected way, but a truly great tool lends itself to uses you never expected.
15. When writing gateway software of any kind, take pains to disturb the data stream as little as possible and never throw away information unless the recipient forces you to!
16. When your language is nowhere near Turing-complete, syntactic sugar can be your friend.
17. A security system is only as secure as its secret. Beware of pseudo-secrets.
18. To solve an interesting problem, start by finding a problem that is interesting to you.
19. Provided the development coordinator has a communications medium at least as good as the Internet, and knows how to lead without coercion, many heads are inevitably better than one.

---

{:.gray}
### 2017-01-19 Week 1 

### Introduction

#### Readings
[cathedral-bazaar.pdf]({{ site.baseurl }}assets/cs451/cathedral-bazaar.pdf)

#### Topics
- course introduction
- syllabus

---

{% comment %}

### 2017-01-19 Week 1 ### Introduction
### 2017-01-24 Week 2 ### Philosophy of Open Source Software Development
### 2017-01-31 Week 3 ### Modern Software Development/Git Preliminaries
### 2017-02-07 Week 4 ### Overview of Modern Software Development Components
### 2017-02-14 Week 5 ### Basic Documentation/Testing 
### 2017-02-21 Week 6 ### Framework(ing) and Project Management
### 2017-02-28 Week 7 ### Project Management
### 2017-03-07 Week 8 ### TBD
### 2017-03-14 Week 9 ### Midterm
### 2017-03-21 Week 10 ### Spring Break
### 2017-03-28 Week 11 ### TBD
### 2017-04-04 Week 12 ### TBD
### 2017-04-11 Week 13 ### TBD
### 2017-04-18 Week 14 ### TBD
### 2017-04-25 Week 15 ### TBD
### 2017-05-02 Week 16 ### TBD
### 2017-05-09 Week 17 ### Final Exam Week

{% endcomment %}


