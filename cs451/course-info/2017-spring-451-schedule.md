---
layout: course_page
title: schedule
permalink: /451/schedule/
parent_course: 451
---

**Spring 2017 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2)

---

{:.green}
### 2017-01-24 Week 2 

### Philosophy of Open Source Software

#### Readings
[cathedral-bazaar.pdf]({{ site.baseurl }}assets/cs451/cathedral-bazaar.pdf)

#### Topics
- discussion of Cathedral and the Bazaar reading
- lessons from the open source software philosophy
- the "prime directives"
- software engineering and complexity
	- a walk through a somewhat complex software project
- git preliminaries

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

#### Git Exercise

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
### 2017-01-19 Week 1 

### Introduction

#### Readings
[cathedral-bazaar.pdf]({{ site.baseurl }}assets/cs451/cathedral-bazaar.pdf)

#### Topics
- course introduction
- syllabus

---


