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
- scheduling
- classic problems in IPC

**Reading** - Chapter 2.4, 2.5, 2.6


Mar 07 Memory Management & Midterm exam
------
- memory management
- midterm exam
 

Mar 14 (Spring Recess)
------

Mar 21 Memory management
------

**Reading** - 

Mar 28 File Systems
------

**Reading** - 

Apr 04 File & I/O
------

**Reading** - 

Apr 11 File & I/O
------

**Reading** - 

Apr 18 Virtualization & The Cloud
------

**Reading** - 

Apr 25 Multiple Processor Systems
------

**Reading** - 

May 02
------
Final Exam 


