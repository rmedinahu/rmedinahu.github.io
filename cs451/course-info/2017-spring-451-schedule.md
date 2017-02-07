---
layout: course_page
title: schedule
permalink: /451/schedule/
parent_course: 451
---

**Spring 2017 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4)

---

{:.green}
### 2017-02-07 Week 4 

### Overview of Modern Software Development Components

#### Readings

- **Chapter 2 & 3** ==> BSE

#### Topics
- prime directives
- introduction of model-view-controller design pattern
- software dev skill: virtual environments and projects
- software dev skill: requirements file
- software dev skill: creating a project shell
- framework analysis - the pyramid framework

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

### Philosophy of Open Source Software

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


