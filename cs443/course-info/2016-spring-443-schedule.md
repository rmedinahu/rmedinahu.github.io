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

----

ps is a command that displays information about all processes currently running in your system. Read man page of ps command. Enter the following commands: (1) ```ps –ef | more``` and (2) ```ps –aux | more```. Both of these will result in displaying a long list of processes. Identify what processes are started when the system is booted, and what processes are started later on. For each process, find out who owns it, what code it is running, and how much CPU/memory it has used.

Now, store the details of all processes owned by root in a file called root- processes-1, and all processes owned by you in a file called my-processes-1. Next, restart your system, and create similar files, root-processes-2 and my-processes-2. Compare root-processes-1 with root-processes-2, and my-processes-1 with my-processes-2. Explain the differences between the two.

----

Simulating a kernel scheduler (using threads), [tutorial](http://www.tutorialspoint.com/python/python_multithreading.htm)


**Reading** - Chapter 2.1, 2.2

**Homework** - _Chapter *1*_ Questions (due feb 15): 10, 12, 17, 18, 28

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


