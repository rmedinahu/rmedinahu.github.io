---
layout: page
title: schedule
permalink: /443/schedule/
---

v.20160125.0rm

CS 443: Operating Systems
-------------------------
*Spring 2016* Schedule of Topics

Jump to week[n] ==> 
[mar 28](#mar-28-memory-management),
[mar 21](#mar-21-memory-management),
[mar 07](#mar-07-midterm-exam), 
[feb 29](#feb-29-scheduling--memory-management), 
[feb 22](#feb-22-interprocess-communication), 
[feb 15](#feb-15-process-management), 
[feb 08](#feb-08-process-management), 
[feb 01](#feb-01-introduction)


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

**Write a python script that will read in a search query (e.g., Google) and report the occurrence of that string in a top generated output file.**

**Reading** - Chapter 1

**powerpoint slides: 

**Homework** - Chapter 2 Questions (due feb 8): 10, 12, 17, 18, 28

Feb 08 Process Management
------
- process basics
- process switching
- threads

**Exercise** 

A shell script is a sequence of shell commands written in an executable script file. Executing this file instructs the shell to execute all commands in the order of their appearance in the script file. There are several shell scripting tutorials available on the web, e.g. search by entering the keywords Linux shell script tutorials. Go through one of these tutorials and then write a shell script that displays various system parameters by using shell commands like who, whoami, date, hostname, etc.

**Reading** - Chapter 2.1, 2.2

**Homework** - _Chapter *1*_ Questions (due feb 15): 10, 12, 17, 18, 28

Feb 15 Process Management
------
- Process Review: multiprogramming, process creation (fork), process states, process table, interrupt handlers
- Thread Review: threads, resource management vs. execution
- ```thread_create```, ```thread_exit```, ```thread_join```, ```thread_yield```
- user-level threads, kernel-level threads
- Operating systems embody multiple **linked data structure**?

**Reading** - Chapter 2.1, 2.2


[Lab Exercises](/145/2016-feb-15-ex/)

----


Feb 22 Interprocess communication
------ 
- IPC 
- race conditions, producer consumer problems
- semaphores and mutexes

**Lab Exercises**: producer/consumer simulation with python and Threading class [let's start here](http://www.tutorialspoint.com/python/python_multithreading.htm)

**Reading** - Chapter 2.3  

Feb 29 Scheduling & Memory Management
------
- scheduling processes and process types
- batch, interactive, real-time
- classic problems in IPC ==> dining philosopher's problem

**Lab Experiments**:

**[1]  (a) Simulating and observing race conditions and (b) implementing critical regions using python threads: See problem 57 on page 178 of text.**

**[2] I/O Bound threads in python. See problem 65 on page 180 of text.** Complete threaded version then write a sequential version. Capture and compare the turn around times from both.

**[3] Comparing CPU-bound and I/O-bound threads**. Write a multithreaded application that contains both types of processes. Compare turn around times between the multithreaded and a sequential versions.

**Reading** - Chapter 2.4, 2.5, 2.6 

*GIL -- Global Interpreter Lock* This is worth knowing!!!

[GIL Contention](http://www.dabeaz.com/GIL/gilvis/)

[GIL Talk](http://www.dabeaz.com/python/UnderstandingGIL.pdf)


Mar 07 Midterm exam
------

[midterm exam questions](/443/midterm-questions/)
 

Mar 14 (Spring Recess)
------

Mar 21 Memory Management
------
- overview
- memory management problems
- address spaces
- swapping
- **in class**: develop simulation of memory allocation/deallocation techniques
- [hw01](/443/hw01/) assigned (yes, homework!)

**LAB**: [/443/mar-21-lab/](/443/mar-21-lab/)

**Reading** - Chapter 3.1, 3.2

Mar 28 Memory Management
------
- virtual memory
- paging
- segmentation

**Reading** - Chapter 3.3, 3.4, 3.5., 3.6, 3.7

Apr 04 File Systems
------

**Reading** - 

Apr 11 I/O & Deadlocks
------

**Reading** - 

Apr 18 Virtualization & The Cloud
------

**Reading** - 

Apr 25 Multiple Processor Systems / Security
------

**Reading** - 

May 02
------
Final Exam 


