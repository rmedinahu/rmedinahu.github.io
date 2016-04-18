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
[apr 18](#apr-18-virtualization),
[apr 11](#apr-11-io),
[apr 04](#apr-04-file-systems),
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
- virtual memory - dealing with bloatware
- paging - big buckets
- segmentation - isolating processes and memory
- [hw02](/443/hw02/) assigned 

[basic-first-fit.py](/assets/basic-first-fit.py)

**LAB**: (continued from last week) [/443/mar-21-lab/](/443/mar-21-lab/)

**Reading** - Chapter 3.3, 3.4, 3.5., 3.6, 3.7

Apr 04 File Systems
------
- user-view of files
- os-view of files (how the user-view is facilitated)
- i-nodes on the terminal
- hard/soft linking
- file system information with ```ls``` and ```df```

**LAB**: file system stats(systems programming)

>	Write a program that starts at a given directory and descends the file tree from that point recording the sizes of all the files it finds. When it is all done, it should print a histogram of the file sizes using a bin width specified as a parameter (e.g., with 1024, file sizes of 0 to 1023 go in one bin, 1024 to 2047 go in the next bin, etc.).


{% highlight python %}
import os, sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)

        else:
            # Unknown file type, print a message
            print 'Skipping %s' % pathname

def visitfile(file):
    print 'visiting', file, 'size', os.stat(file).st_size

if __name__ == '__main__':
    walktree(sys.argv[1], visitfile)
{% endhighlight %}

OR 

>	Write a program that scans all directories in a UNIX file system and finds and locates all i-nodes with a hard link count of two or more. For each such file, it lists together all file names that point to the file.

Example: ```find . -inum 1448239```

**Reading** - Chapter ```4.1-4```

python lib ==> [https://docs.python.org/2/library/stat.html](https://docs.python.org/2/library/stat.html)


Apr 11 I/O
------
- DMA -- Direct Memory Access
- interrupts
- device drivers
- Disks
- [hw04](/443/hw04/) assigned 


**LAB**

Write a program to implement the three disk-arm scheduling algorithms. Write a driver program that generates a sequence of cylinder numbers (0–999) at random, runs the three algorithms for this sequence and prints out the total distance (number of cylinders) the arm needs to traverse in the three algorithms.

**Reading** - 5.1-5.4

Apr 18 Virtualization
------
- python virtualenv -- the basic idea, the ```JVM``` is another
- (Virtual Machine Monitor) hypervisor 1 & 2
- virtualization and the cloud
- Demo: Amazon EC2 
- [hw05](/443/hw05/) assigned

Links:
[ec2 info](https://aws.amazon.com/ec2/)

[british ec2](https://youtu.be/TsRBftzZsQo)

**LAB & Homework**

see [hw05](/443/hw05/)

**Reading** - 7, online texts

Apr 25 Multiple Processor Systems 
------

**Reading** - 

May 02 Security 
------

**Reading** - 

Final Exam
------
**Online during finals week.**

