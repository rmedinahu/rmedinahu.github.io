---
layout: course_page
title: schedule
permalink: /436/schedule/
parent_course: 436
---

**Fall 2016 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6)

---


{:.green}
### 2016-09-27 Week 6

#### Readings

[Bootstrap](http://getbootstrap.com/)

[Web Style Guide 3rd ed. - CHAPTER 11 - Graphics](http://www.webstyleguide.com/wsg3/11-graphics/index.html)

#### Topics
- socio-technical UI
- design problems:
	* visibility: *Who am I interacting with?*
	* awareness: *What are we doing?*
	* identity: *Who am I?*
	* time: *Asynchronous or Synchronous*
	* shared objects: *What objects do we share and don't share?*

- design context:
	* real time communication and/or collaboration
	* asynchronous communication and/or collaboration
	* multiple channels for communication and/or action

{:.blue}
#### Workshop: Chat User Interface

###### This is homework. **Submit to D2L dropbox by next Tuesday before class.**

**Required Libraries:** [jQuery core library](http://jquery.com/),  [Bootstrap getting started](http://getbootstrap.com/getting-started/), [Font Awesome Icons](http://fontawesome.io/get-started/)

Write a single HTML page that simulates a chat room. The UI should contain an input widget to enter a chat message. On "send", use jQuery/javascript to append the new message to a list of messages in a separate container. Once a message has been "sent" clear the chat input widget to accept another message.

1. Must use Bootstrap and grid layouts.
2. Must use icons to provide clues to the organization of the UI. (see Font Awesome linked above).
3. Chat messages must scroll when message list grows long.

{% highlight html %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title></title> 
    
    <script src="https://use.fontawesome.com/31ce935913.js"></script>


    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"> 
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <div id="data-target" class="col-md-12"></div>
        </div>
    </div>

<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

<script type="text/javascript">
    $( document ).ready(function() {
        
    });  
</script>
</body>
</html>
{% endhighlight html %}


---


{:.gray}
### 2016-09-20 Week 5

#### Readings

[Bootstrap](http://getbootstrap.com/)

[Web Style Guide 3rd ed. - CHAPTER 11 - Graphics](http://www.webstyleguide.com/wsg3/11-graphics/index.html)

#### Topics
- direct manipulation
	* leverages humans' efficient hand-eye coordination
- drag and drop
	* mouse and touch
	* freehand vs. constrained
- design problems:
	* target object large enough for "grasping"
	* cause and effect
	* affordances
- design context:
	* sorting items
	* adding to a list or set of choices
	* where else?

{:.blue}
#### Workshop: Shopping and Sorting with Drag and Drop


###### This is homework. **Submit to D2L dropbox by next Tuesday before class.**

[jQuery core library](http://jquery.com/)

[jQuery ui library](https://jqueryui.com/)

[Bootstrap getting started](http://getbootstrap.com/getting-started/)

[Web Style Guide 3rd ed. - CHAPTER 11 - Graphics](http://www.webstyleguide.com/wsg3/11-graphics/index.html)


Write a single html page that simulates an interface for selecting movies from a set of choices. A selected movie should be dragged to a *shopping cart* container. The user can *reorder* the items in the shopping cart by priority at any time. Movies should be represented with images and text.

1. Take a look at other shopping ui's (e.g., amazon, netflix, etc.) for ideas.
2. You will need at least **12** sample items (e.g., movie images) but definitely consider how your design will scale with hundreds or thousands of items.
3. Consider the best way for someone to *browse* the sample items. Remember that users will be *dragging* selections to the shopping cart so make sure that is easy to get to!
4. Bootstrap framework is required!

#### The following should help you get started with drag and drop.
{% highlight html %}
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>UI Draggable</title>
  <style>
    .draggable { border: 1px solid black; width: 50px;}
    #dropzone { width: 200px; height: 150px; background-color: #cccccc; border: 1px solid black;}
  </style>
  
</head>
<body>

<div>

  <h3>Draggables</h3>
  <p><span id="draggable1" class="draggable">item 1</span></p>
  <p><span id="draggable2" class="draggable">item 2</span></p>
  <p><span id="draggable3" class="draggable">item 3</span></p>


  <h3>Drop Zone</h3>
  <div id="dropzone">
    <ul id="sortable"></ul>
  </div>
</div>

<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script type="text/javascript">
  $( document ).ready(function() {
    $( ".draggable" ).draggable();
    $( "#sortable" ).sortable().disableSelection();
    
    $( "#dropzone" ).droppable({
        drop: function( event, ui ) {
          $("#sortable").append( "<li>"+ui.draggable.text()+"</li>" );
          ui.draggable.remove();
          $("#sortable").hide().fadeIn('fast')
        }
    });
  });  
</script>
</body>
</html>
{% endhighlight %}


---

{:.gray}
### 2016-09-13 Week 4

#### Readings

[Bootstrap](http://getbootstrap.com/)

[Web Style Guide 3rd ed. -CHAPTER 4](http://www.webstyleguide.com/wsg3/4-interface-design/index.html)

#### Topics
- data entry in forms (sequencing, widget selection, minimize errors)
- menu design
- menu design for ...?
	* browsing
	* accessing
	* searching
	* novices or experts or both

- menu design issues
	* task related
	* phrasing of items
	* sequence of items
	* layout
	* selection mechanisms

- menu hierarchies
	* reduce # of required actions 
	* allow rapid selection (experts?)
	* view potential actions (novices?)

- menu guidelines
	- breadth over depth
	- levels <= 3
	- trees: items in parent should TITLE items in child
- menu maps: birds eye view

#### Workshop: Eyeball Evaluation of EMR Form, Bootstrap & A Library UI

[Bootstrap getting started](http://getbootstrap.com/getting-started/)

##### Eyeball evaluation
- choose an html file from the list [here]({{ site.baseurl }}assets/emrsamples/) and evaluate the design based on:
	
	**Record your metrics on scratch paper for discussion.**

	1. number of actions required to complete the form
	2. the logical order of fields (very logical or illogical). This is subjective but *who* would be better tasked with evaluating this metric?
	3. display of form on small screen dimensions (resize the window or use the browser tools to simulate small screen devices). Evaluate whether the form is easy or more difficult to read at small screen sizes.

##### Library UI

1. First, address the questions with a partner and note your conclusions in a file or scratch paper (save this for later)

	**Guiding questions for your work:**

	* What are the services provided by the library (view the real library website for background)
	* What are the levels of expertise for users (novice, expert?)
	* Who are the users (students, professors, public, library personnel?)
	* What kind of actions do users perform at a library website?


2. Next, use the ```bootstrap``` framework to design and implement the homepage for the NMHU library. Focus your work on the design of the menus that users will view when accessing the library website. 

>Note: Do not simply replicate the design of the menus but try to devise another menu design based on our class discussion and your own creativity. Review bootstrap components: ```dropboxes```, ```navs```, ```navbars```

Boilerplate ...

	<!doctype html>
	<html lang="en">
	<head>
	    <meta charset="utf-8">
	    <title>Title</title>
	    <meta name="viewport" content="width=device-width, initial-scale=1">
	</head>
	<body>
	    <h1></h1>
	</body>
	</html>

---


{:.gray}
### 2016-09-06 Week 3

#### Readings

For reference:

[US Government Standards for Web UI](https://standards.usa.gov/)

[Web Style Guide 3rd ed.](http://www.webstyleguide.com/wsg3/)

[Accessible Rich Internet Applications (ARIA)](https://www.w3.org/TR/wai-aria/)

#### Topics

- Using design standards and guidelines
- Using UI frameworks -- don't reinvent the wheel
- data entry flow (how many clicks does it take?)
- data constraints/validation
- action handling
- grid layouts -- responsive design

#### Workshop: CSS Frameworks for Consistency and Accessibility

**A UI for gathering patient information during emergency triage. What are some considerations that need to be made in this context?**

**Reference**

- [https://standards.usa.gov/getting-started/developers/](https://standards.usa.gov/getting-started/developers/)
- [Form design ==> Web Style Guide 3rd ed.](http://www.webstyleguide.com/wsg3/10-forms-and-applications/3-designing-web-applications.html)

**Description**

Create a single web page with a heading titled with your name followed by "Patient Entry". This page will contain a form that collects information about a patient currently being admitted to ER. Collect the following information to establish the patient Electronic Medical Record (EMR).

- current vitals(conscious, unconscious)
- current date and time
- first and last name
- 4 digit human identifier
- injury category (make up some categories)
- injury description
- emergency status (gray=stable, yellow=somewhat unstable, red=unstable)
- on submit of the form, gather the data and display it in a **confirm** dialog box.

**Requirements**

1. Use the US government web standards/guidelines.
2. Use the US government web standards/guidelines developer kit (linked above).
	- make sure to use the ```grid``` layout
3. Decide on what you think is the *optimal* ordering of the input widgets.
4. Use ```jQuery``` for action/event handling

Submit your completed html page (submit only one file) to Desire 2 Learn Dropbox ==> Homework 2.


---


{:.gray}
### 2016-08-30 Week 2

#### Readings

[Human Computer Interaction - brief intro](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/human-computer-interaction-brief-intro)

#### Topics
- About HCI (John Carroll's intro)
- Guidelines, principles, and theories
- UI Contexts ==> direct manipulation, data entry, information display/visualization, interaction devices, command languages, collaborative and social media 
- UI Users (novice <--> expert)

#### Sample Guidelines
- [https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/OSXHIGuidelines/index.html](https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/OSXHIGuidelines/index.html)
- [https://developer.apple.com/ios/human-interface-guidelines/](https://developer.apple.com/ios/human-interface-guidelines/)
- [https://developer.apple.com/watch/human-interface-guidelines/](https://developer.apple.com/watch/human-interface-guidelines/)
- [https://developer.android.com/design/index.html](https://developer.android.com/design/index.html)
- [https://design.ubuntu.com/apps](https://design.ubuntu.com/apps)
- [https://msdn.microsoft.com/library/windows/desktop/dn742479.aspx](https://msdn.microsoft.com/library/windows/desktop/dn742479.aspx)
- [https://standards.usa.gov/](https://standards.usa.gov/)

#### Principles: Eight Golden Rules of Interface Design
1. Strive for consistency
2. Cater to universal usbility
3. Offer informative feedback
4. Design dialogs to yield closure
5. Prevent errors
6. Permit easy reversal of actions
7. Support internal locus of control
8. Reduce short term memory load

#### Workshop: Coding Data Entry UI with HTML and javascript and jQuery

**A UI for gathering information from student applying for a job.**

[W3 Schools HTML ref](http://www.w3schools.com/html/default.asp)

[jQuery](http://jquery.com/)

[jQuery quick start](https://learn.jquery.com/about-jquery/how-jquery-works/)

1. Create a project folder for this workshop
2. Download the following and save to your project folder
	- Copy and paste the following HTML template into a new html file on your machine.

- [Download boilerplate.html (or click then save file as ...)]({{ site.baseurl }}assets/cs436/boilerplate.html)
- [Download jQuery library](https://code.jquery.com/jquery-3.1.0.min.js)

3. Using html widgets, create an HTML form that gathers the following information from a student.
	- first and last name
	- today's date
	- gender
	- a paragraph describing why they want the job
	- preferred salary
	- years of prior experience
	- degree (associates, bachelors, masters, phd)
	- degree field (CS, Biology, etc.)

4. After submitting the form, the UI should present the information in a confirmation dialog (accepting or canceling the application)

5. Demonstrate your UI to instructor.


---

{:.gray}
### 2016-08-23 Week 1 

#### Readings
[Human Computer Interaction - brief intro (before week 2)](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/human-computer-interaction-brief-intro)

#### Topics

- About the field of Human Computer Interaction
- Organization of the course
- A simple analytic framework
- Group: Paper/pencil evaluation of a UI
- Programming Pre-assessment (for those who haven't taken it yet)

#### Survey says ....
- How many of you have built a user interface and for what purpose?
- What was the scope? (a small aspect of a program or function or a comprehensive front-end to a large complex application)
- What was the scale? (used by MANY users or just a few or just YOU)

#### What is HCI?
- Probable answer A ==> *Programming the user interface so that a human can use our system.*
- Probable answer B ==> *Use an application library to code buttons, menus, and windows so that a human can use our system.*

*... but it's more nuanced than that!*

- a principled and carefully thought out approach (analysis!) to designing for humans and their capabilities
	* cognitive, physical, sensory, and (nowadays) social
- fundamentally **interdisciplinary**
	* psychology/cognitive science, software engineering, graphic design, behavioral sciences, business/economics, natural sciences
- field of **research** - people **write** dissertations in the field
	* Example: Dr. Medina's dissertation!
- field of **practice** - people **construct** UI's following principles and guidelines (*usually from research!*)
- so, HCI refers to a bunch of different concepts and it is evolving!
	
	BEFORE: single user systems, minimal networks, non-distributed (stand alone), closed
	
	NOW: collaborative systems, massive scale, distributed networks, open

	BEFORE: single db or data stores (non distributed)

	NOW: cloud storage, cloud services, distributed data, massive amount and **types!** of data - "big data"

where do we begin to deal with this evolution beyound windows, menus, and buttons? A single unifying abstraction, of course!

#### FUNDAMENTAL UNIFYING ABSTRACTION FOR THE COURSE

```TECHNOLOGY MEDIATION``` 

- mediating actions, thoughts, ideas, and joint (social) activity
- a continuum: 
	* low level to high level - action (a ```submit``` button) to thought and inquiry (analytics)
	* individual user to social network
	* personal data (contact list manager) to massive social data stores (voting analytics, twitter feeds) 

#### Organization of the course

**FOUNDATIONS**

	develop your understanding of HCI principles and techniques common to the field and to software engineering in general

**PRACTICE**
	
	learn how to use tools for designing and implementing interactive user interfaces for relatively large or complex data sets.

	appreciate the array of current technological capabilities for supporting mediation
	
	Examples ==> visualization, large data displays, interactivity, gesture, gaze and sound mediation.

**INTELLECTUAL**

	develop analytic skills for doing principled and carefully thought out UI development for mediating human computer interactions

#### A Simple Framework Classroom Exercise

1. Identify/characterize the user(s) or ```stakeholders``` of the NMHU (banner) online class schedule
2. Brainstorm and list potential ```goals``` the stakeholders may have regarding the system
3. For each goal, decide on a rating from 0 to five stars (five stars is highest rating) of how well the existing system meets that goal. This is subjective of course but let's start with our intuitions!
4. For at least one goal that received a poor rating, discuss among yourselves how you would improve it to elevate its rating.

#### Preassessment (if you haven't done this for me in another course this semester)

Python pre-assessment ==> [pretest.py]({{ site.baseurl }}assets/cs350/pretest.py)


[comment]:### 2016-09-06 Week 3 
[comment]:### 2016-09-13 Week 4 
[comment]:### 2016-09-20 Week 5 
[comment]:### 2016-09-27 Week 6 
[comment]:### 2016-10-04 Week 7
[comment]:### 2016-10-11 Week 8 
[comment]:### 2016-10-25 Week 9
[comment]:### 2016-11-01 Week 10 
[comment]:### 2016-11-08 Week 11
[comment]:### 2016-11-15 Week 12
[comment]:### 2016-11-22 Week 13
[comment]:### 2016-11-29 Week 14

