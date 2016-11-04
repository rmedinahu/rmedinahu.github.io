---
layout: course_page
title: lab 11
permalink: /350/lab11/
parent_course: 350
---

### 2016-11-03

### Buffer Overflow and Stack Analysis With GDB

Today's lab will focus on techniques for analyzing memory stacks to learn about stack overflows.

We will use Kali Linux to simulate a buffer overflow attack. We will also use the gdb debugger to analyze the stack.

### Materials Needed:
- Chapter 3 of Hacking 2nd ed. We will follow the techique beginning on page **122** through **128**.
- The source code files for Hacking 2nd ed. [download source files](http://www.nostarch.com/download/booksrc.zip)

### Procedure:
- Beginning page 122, work through the simulation as described in the text. **NOTE**: use the ```clang``` compiler rather than gcc for the compilation steps:

Example:

> clang -g -o auth_overflow auth_overflow.c

*The -g option is for use with the gdb debugger*

- You will need to access two source files for the simulation: *auth_overflow.c* and *auth_overflow2.c* 

### Experiment:
After proceeding through the sequence of commands listed in the Hacking text, you will then attempt to write a value (**7**) to the ```auth_flag``` memory location. Use *auth_overflow.c* for this part of the experiment.

### Topics:
- Simulating a buffer overflow attack
- [Kali Linux](https://www.kali.org/) - a Debian distribution for penetration testing  
- [Download page](https://www.kali.org/downloads/) ==> download Kali Linux 64 bit
- [Installation instructions various platforms](http://docs.kali.org/downloading/kali-linux-live-usb-install)



