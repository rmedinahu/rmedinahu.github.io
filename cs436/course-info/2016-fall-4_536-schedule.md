---
layout: course_page
title: schedule
permalink: /436/schedule/
parent_course: 436
---

**Fall 2016 Schedule of Topics**

Jump to week[n] ==> [1](#week-1), [2](#week-2), [3](#week-3), [4](#week-4), [5](#week-5), [6](#week-6), [7](#week-7), [10](#week-10), [11](#week-11), [12](#week-12)

---

{:.green}
### 2016-11-15 Week 13

#### Readings

#### Topics
- Evaluating User Interfaces -- linking **use case** <==> **design** <==> **implementation**
- Layouts, grouping by task, efficient use of space
- Demonstration of filtering and sorting submissions

{:.blue}
#### Workshop: Sliders in Space

[jqueryui](https://jqueryui.com/)

[Bootstrap](http://getbootstrap.com/)

[Metafizzy Isotope](http://isotope.metafizzy.co/)

###### This is homework. **Submit to D2L dropbox by next Tuesday, November 22 before class.**

This projects is yet another extension to filtering and sorting to manage large data sets. You are going to use the same data from the last assignment as well as the filtering and sorting you've already implemented. The task for this is to:

###### Use Cases:
1. filter courses by semester
2. filter courses by enrollment

###### Requirements:
a. use a slider widget to filter courses by semester

b. use a slider widget to filter courses by enrollment. (This is already in the data.)

c. menus to limit the filtering and sorting toolbar to the top row of the screen. (We need to optimize screen space!!!)

d. ensure that your ui provides feedback on the selected filter.


---


{:.gray}
### 2016-11-08 Week 12

#### Readings

[Bootstrap](http://getbootstrap.com/)

[Metafizzy Isotope](http://isotope.metafizzy.co/)

#### Topics
- Evaluating User Interfaces -- linking **use case** <==> **design** <==> **implementation**
- data metrics:
	- video (objective)
	- eye tracking (objective)
	- log files (objective) E.g, UGU, 
	- surveys
- Examples:
	- UGU/VMT
	- Tag Clouds video w/Elan
	- Tobii

{:.blue}
#### Workshop: EXTENDED to Nov 15. Data Wrangling With Filtering and Sorting  (see below)

[A Working Example to Start With (filter-sort.html)]({{ site.baseurl }}assets/cs436/filter-sort.html)

[Python file for preprocessing the csv file referenced below ==> cs-2005-2015-wrangle.py]({{ site.baseurl }}assets/cs436/cs-2005-2015-wrangle.py)


---


{:.gray}
### 2016-11-01 Week 11

#### Readings

[Bootstrap](http://getbootstrap.com/)

[Metafizzy Isotope](http://isotope.metafizzy.co/)

#### Topics
- Simple data wrangling for prototyping.
- Basic python

{:.blue}
#### Workshop: Data Wrangling With Filtering and Sorting

###### This is homework. **Submit to D2L dropbox by next Tuesday, November 8 before class.**

You are going to refactor Filtering and Sorting homework so that it loads sample data. Use cases still apply. 

a. Download [cs-2005-2015.csv]({{ site.baseurl }}assets/cs436/cs-2005-2015.csv) containing sample course data. You will need to preprocess this list of courses using python as demonstrated in class to produce an array:

```[["200610", "Fall Semester 2005", "101", "Living with Computers", "37"], [...]]```

b. The array should be written to a local file using ```json.dumps(data)```.

c. Copy and paste the array in the processed file into your html file (at the bottom of your script tag) then process the array as shown below.:

>	var DATA = [["200610", "Fall Semester 2005", "101", "Living with Computers", "37"], ["200610", "Fall Semester 2005", "101", "Living with Computers", "39"], ["200610", "Fall Semester 2005", "135", "Select Top in Comp Science", "16"], ...];
>	for (i = 0; i < DATA.length; i++) { 
>		var row = "<li>";
>		for (j = 0; j < DATA[i].length; j++) { 
>			row += DATA[i][j] + " ";
>		}
>		row += "</li>";
>	}

---

{:.gray}
### 2016-10-25 Week 10

#### Readings

[Bootstrap](http://getbootstrap.com/)

[Metafizzy Isotope](http://isotope.metafizzy.co/)

#### Topics
- managing large data sets.

{:.blue}
#### Workshop: Data Filtering and Sorting

###### This is homework. **Submit to D2L dropbox by next Tuesday, November 1 before class.**

You are going to *prototype* a UI that helps a user browse/search a large number of items. You will use filtering and sorting techniques and the isotope library to design an efficient UI for the following use cases. These again are in the context of a scheduling application.

##### Use Cases:

1. Filter courses by name (e.g. show all courses that begin with the letter a).
2. Filter courses by course number (e.g. 245, 351, etc.)
3. Sort courses by name in descending or ascending order.
4. Show all courses.
5. Filter courses by semester(s) previously taught in the last four semesters. (e.g., spring 2016, fall 2015, spring 2015, fall 2014). A course may have been taught in more than once in the previous four semesters.

##### Starter code:

{% highlight html %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

</head>
<body>
	<div class="container-fluid">
	    <div class="row"><p class="lead">Metafizzy Sample</p></div>

		<div class="row button-group filters-button-group">
			<div class="col-md-4 btn" data-filter="*">show all</div>
			<div class="col-md-4 btn" data-filter=".a-f">a-f</div>
			
			<button id="sort-btn" class="col-md-4 btn" data-sort-by="name" data-order="dsc">sort</button>

		</div>

		<div id="list" class="row lead filterdata">
			<div class="col-md-12 item name a-f">Adv Computer ProgrammingAdv</div>
			<div class="col-md-12 item name a-f">C and Unix</div>
			<div class="col-md-12 item name a-f">Computer Networks</div>
			<div class="col-md-12 item name">Intro to Computer Science</div>
			<div class="col-md-12 item name">Hands on UNIX</div>
			<div class="col-md-12 item name">Human-Computer Interaction</div>
			<div class="col-md-12 item name">Image Processing</div>
			<div class="col-md-12 item name">Living with Computers</div>
			<div class="col-md-12 item name">Multimedia Project Development</div>
			<div class="col-md-12 item name">Multimedia Programming</div>
			<div class="col-md-12 item name">Network Security</div>
			<div class="col-md-12 item name">Parallel and Distributed Program</div>
			<div class="col-md-12 item name">Senior Project Implementation</div>
			<div class="col-md-12 item name">Systems Design and Analysis</div>
			<div class="col-md-12 item name">Synthesis of Media Arts and CS</div>
		</div>
	</div>

    <script   src="https://code.jquery.com/jquery-2.2.4.min.js"   integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>


	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	
	<script type="text/javascript" src="js/isotope.pkgd.min.js"></script>

    <script type="text/javascript">
		$( document ).ready(function() {
			
			var $grid = $('.filterdata').isotope({
				  itemSelector: '.item',
				  layoutMode: 'fitRows',
				  
				  getSortData: {
					name: '.name' 
				}				  
			});		

			// bind filter button click
			$('.filters-button-group').on( 'click', '.btn', function() {
				var filterValue = $( this ).attr('data-filter');
				$grid.isotope({ filter: filterValue });
			});

			// bind sort button click
			$('#sort-btn').on( 'click', function() {
				var sortbyval = $( this ).attr('data-sort-by');
				var order = "";
                if ($(this).attr("data-order")==="asc") {
                    order = true;
                    $(this).attr("data-order", "");
                } else {
                    order = false;
                    $(this).attr("data-order", "asc");
                }

				$grid.isotope({ sortBy : sortbyval, sortAscending: order });
				console.log('sorting?' + sortbyval);
			});

		});  
    </script>
</body>
</html>

{% endhighlight %}

---

{:.gray}
### 2016-10-04 Week 7

#### Readings

[Bootstrap](http://getbootstrap.com/)

[Web Style Guide 3rd ed. - CHAPTER 11 - Graphics](http://www.webstyleguide.com/wsg3/11-graphics/index.html)

#### Topics
- use cases
- prototypes

{:.blue}
#### Workshop: Scheduling Prototype

###### This is your midterm exam. **Submit to D2L dropbox by next Wednesday, October 12 before 5pm.**

You are going to *prototype* a UI to assist CS faculty with developing a schedule for the upcoming semester. This UI should allow the user to make selections regarding what class is taught and by who. The result of the selections should produce a dialog box containing a list of each course selected and who is going to teach it. Your prototype should handle a schedule with a minimum of 6 courses taught by a minimum of 2 professors. In addition to your prototype you will need to provide a rationale for your design. This will be a separate html page containing your explanation of the design (why you used certain components, etc.). Link the rationale page from your prototype.

Here's a course listing: [sample-courses.txt]({{ site.baseurl }}assets/cs436/sample-courses.txt)

Below are *use cases* that your prototype should address:

##### Use Cases:
0. User creates a new semester schedule by selecting courses and instructors.

1. User can review a history of course offerings by semester, going back 5 years (10 semesters).

2. User can review a listing of courses in the catalog where each course listing contains the course number and title.

3. User can select a course from the course listing to add to the new semester

4. User can select a instructor from a listing of instructors to associate with a course (in the new schedule).

5. User tries to build schedule so that courses that have not been offered in a "long" time are given priority for the new schedule.

##### Grading Criteria:

* +50 each of the above use cases are reflected in the prototype
* +10 Bootstrap framework is used including grid layouts
* +10 jQuery is used to handle simulated actions
* +10 for each component, specify which use case the component addresses. You can use a ```popup``` indicate this.
* +20 a short html page that explains the *rationale* for your design. This page is separate from the prototype but should be linked from the prototype.

##### Submit prototype and rationale pages to d2l.

---

{:.gray}
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

