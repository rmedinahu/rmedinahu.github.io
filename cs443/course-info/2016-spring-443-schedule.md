---
layout: page
title: 
permalink: /443/schedule/
---

v.20160125.0rm

CS 443: Operating Systems
-------------------------
*Spring 2016* Schedule of Topics

Jan 25 (no class)
------  

Feb 01 Introduction
------
- syllabus
- major topics of study (process management, memory management, i/o)
- architecture overview
- abstractions - the OS hides the hardware
- control - the OS manages and controls the hw resources
- multiplexing - time (slicing) and space (concurrent allocation)
- study is not about UI
- history
- multiprogramming --> timesharing
- MULTICS - timesharing computing server - 60's
- Device control - cpu, mem, i/o - interrupts

Using Unix

- the shell
- commands: processes, memory management, i/o
- system

**Exercises**

*Process Data - top command*
	
	mac : $ top -stats pid,ppid,command,cpu,th,pstate,time -l 1
	linux: $ top -stats pid,ppid,command,cpu,th,pstate,time -b

- Analyze top command to find out the process tree for the bash process. Another running application?

*Programming API - Scripting the OS*

- system calls in python using **subprocess** and **envoy**
- learn how to read the status codes returned from system calls.

[python os module](https://docs.python.org/2/library/os.html)

[python subprocess module](https://docs.python.org/2/library/subprocess.html)

[subprocess for sys admins](http://www.pythonforbeginners.com/os/subprocess-for-system-administrators) 

[envoy wrapper for subprocess](http://www.pythonforbeginners.com/envoy/how-to-use-the-envoy-wrapper)

[envoy package](https://github.com/kennethreitz/envoy)

*Write a python script that will accept a search query on standard input and report the occurrence of that string in a top generated output file.*

**Reading** - Chapter 1

Feb 08 Process Management
------

**Reading** - 

Feb 15 Process Management
------

**Reading** - 

Feb 22
------
a. 

**Reading** - 

Feb 29
------
a. 

**Reading** - 

Mar 07
------
a. 

Midterm
 

Mar 14 (Spring Recess)
------

Mar 21
------
a. 

**Reading** - 

Mar 28
------
a. 

**Reading** - 

Apr 04
------
a. 

**Reading** - 

Apr 11
------
a. 

**Reading** - 

Apr 18
------
a. 

**Reading** - 

Apr 25
------
a. 

**Reading** - 

May 02
------
Final Exam 


