cs145 Jan 22 2016 

Lab 01: Programmer Toolbox & Your First Program
===

This lab is an *ice breaker* intended to introduce the tools you will use throughout the course. After this lab everyone should feel comfortable setting up and using your working environment to begin programming.

Lab Tools
---

* All machines are running Ubuntu Linux. 
* Participating in lab will always require:
    1. An open web browser (this is where you will find the lab sheet in D2L). We also access the web for information while we program. For example, we may refer to online documentation and tutorials to help us with our code.
    2. A terminal window (aka "Command Prompt" on Windows). This our access to the operating system and where we *run* our programs.
    3. An **Integrated Development Environment**. In this course I use and recommend an application named **Sublime Text 2 or 3** but you may use your preferred application if you have one.


Desire2Learn Submission Protocol and Email Setup
---

https://nmhu.desire2learn.com


Python Programming Language Hello World Demo
---

https://www.python.org/

* Python in REPL mode (Interactive Interpreter)
    * Allows you to enter python instructions and immediately view the result. This is commonly referred to as a **REPL** or *Read->Evaluate->Print->Loop*.
    * Start the python interpreter by simply typing:

        $> python
        
* Python in script mode
    * Using the **IDE**
    * Managing your source code files on Linux terminal
        * **ls -l** - view files in a directory (or folder)
        * **cd <PATH>** - change to a directory indicated by PATH
    * Running a python script
    
        
        $> python mypythonscript.py
        

The Python Turtle Docs
---
https://docs.python.org/2/library/turtle.html
    

Exercises
---
**Do the following in the order indicated below. When finished, please submit one python file (e.g., prg1.py) to D2L dropbox for this lab.**

1. Using IDE, create a new empty python source file with filename containing your first name and last initial followed by .py extension. **Make sure you remember what folder you save the file in!**

    - After creating the file, go to the terminal and make sure the terminal is currently in the directory where you saved your file.

2. Try executing the following set of instructions in your file.


    import turtle 

    alex = turtle.Turtle() 
    alex.shape('turtle')  

    alex.forward(50)
    alex.right(90)

    turtle.exitonclick()
	

3. If the instructions above worked. Try the following:
    **Please refer to the Python Turtle docs at the link above as you attempt the following modifications to your file created in the previous step.**
    
    **Please attempt the following in an incremental way. Eg., your program will have the turtle drawing a square and circle and anything else you may have added.**
        
    - Change the shape of the turtle.
    - Get the turtle to move forward 75 units.
    - Get the turtle to turn right 90 degrees and move 75 units.
    - Get the turtle to draw a square that is 75 units wide and 75 units long.
    - Get the turtle to draw a circle
    - Try any other modification you may have found interesting from the turtle docs.

Submit ONE File (the file you created for the exercises) to the D2L Dropbox Before Leaving Lab
---







