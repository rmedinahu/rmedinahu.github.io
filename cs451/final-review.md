---
layout: course_page
title: Final Exam Review
permalink: /451/final-review/
parent_course: 451
---

## Final Review

- Exam will consist of no more than 25 multiple choice questions. I will reuse some questions from the midterm exam. Be sure to study the **midterm** in D2L. You should still have access to the midterm. Each question includes your response and the correct answer.

> (1) Choose quizzes from Assessment menu, (2) find midterm exam in list, (3) select submissions from quiz menu, (4) select attempts. 

- HINT: review the weekly schedule for details

#### Git
- repository: working copy, remote copy
- branches vs. forks
- procedures for collaboration (pull and push)
- conflict resolution 

#### Testing
- pytest vs. unittest vs. doctest
- why unit testing contributes to better programs?

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

**New since midterm**

#### Low Level Design
- inheritance
- method override

#### Design Patterns
- [(DP) Design Patterns - chapter 1]({{ site.baseurl }}assets/cs451/gamma-etal-ch-1.pdf)
- understand ```composition``` pattern ==> why do the authors consider composition a better strategy for reusability than inheritance? (DP: p.18)
- understand the ```template method``` pattern (generics)
- consider three types of software that can benefit from design patterns (DP: p.25) and **why**:
	application programs, toolkits, frameworks

#### Frameworks and Django
- [Django Generic Views](https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/)
- [Django Class Based View Inspector](https://ccbv.co.uk/)
- model-view-controller (MVC) architectures
- how django handles web requests (client->server->urls->view->model->view->server->client)
- understand how django generic views utilize the ```template method``` design pattern (see week [15](#week-15))
- what is a method resolution order


