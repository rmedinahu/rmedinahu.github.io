---
layout: page
title:
permalink: /443/final-exam-questions/
---

CS 443 Final Exam
----------

2016-05-09

*Instructions*

In a separate text file (seriously, a ```.txt``` file please), provide responses to the following questions. When done, save the text file with your name in the filename and upload to D2L final exam drop box. Please submit your responses by **Friday May 13 @ 5pm**. 

You may use any materials available to answer the questions.


Chapter 01
----------
1. a) What are system calls? b) Name and briefly describe two system calls.

2. What is meant by a trap instruction?

3. What are key differences between kernel mode and user mode in a layered operating system?


Chapter 02
----------
1. What is a process and why is it a central concept in operating systems?

2. How are processess typically created?

3. What are the three main process states?

4. What is meant by the term *multiprogramming* and how is it related to the concept of *process management*?

5. How are processes and threads different and how are they the same?

6. Why do we consider kernel trap instructions as incurring a relatively high performance cost?

7. What is a semaphore?

8. Describe an example of a *cpu bound* and an example of an *i/o bound* process. Why would it be important for a scheduling algorithm to "know" this process characterization?

9. What is a mutex?


Chapter 03
----------
1. Explain in a paragraph the notion of an *address space* and why it is necessary.

2. The text describes two techniques for allocating and deallocating free memory to requesting processes -- bitmaps and linked lists. Compare and contrast these two approaches. The text suggests an argument against bitmaps. What is it?

3. Briefly describe each of the five memory allocation algorithms discussed in section ```3.2.3```. Compare and contrast all five based on the notion of fragmentation.

4. Identify and describe the underlying reasoning and strategies behind ```aging``` and ```WSClock``` page replacement algorithms.

5. Work out a clear explanation of ```paging```, ```page faults```, and ```page tables```

6. What is ```segmentation``` and what problem does it address?


Chapter 04
----------
1. What is an ```inode``` and what is the implication of ```hard``` and ```soft (aka symbolic)``` links on inodes? What are the security implications of using ```hard``` links?

2. What is ```defragmentation``` and what problem does it solve?


Chapter 05
----------
1. Compare and contrast the three disk arm scheduling algorithms discussed in the text.

2. Provide a brief and sensible explanation of a ```DMA``` (Direct Memory Access) controller. What is the purpose of a DMA Controller?


Chapter 07
----------
1. Please list at least a pro and con for the use of both Hypervisors type 1 and 2? Of the two, which one is the most portable (on different hardware)?

2. Pages 475 and 476 in the text discuss the idea of sensitive and privileged instructions. Please explain in your own words how this key difference was the reason why earlier architectures were not **virtualizable**.

Chapter 08
----------
1. Discuss the pros and cons of the three types of multiprocessor systems discussed in the text (multiprocessor, multicomputer, distributed systems). 








