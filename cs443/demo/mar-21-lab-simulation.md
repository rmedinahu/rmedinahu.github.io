---
layout: course_page
title:
permalink: /443/mar-21-lab/
parent_course: 443
---

Simulation Exercise 2: Main Memory Allocation
----

**Goal**: To simulate and evaluate different memory allocation/deallocation techniques, ```first fit```, ```next fit```, ```best fit```, and ```worst fit```, when a linked list (**see below for implementation on this**) is used to keep track of memory usage.

Assume that the memory is 256 KB and is divided into units of 2 KB each. A process may request between 3 and 10 units of memory. Your simulation consists of three components: Memory component that implements a specific allocation/deallocation technique; request generation component that generates allocation/deallocation requests; and statistics reporting component that prints out the relevant statistics. The Memory component exports the following functions:

>	1. int allocate_mem (int process_id, int num_units): allocates num_units units of memory to a process whose id is process_id. If successful, it returns the number of nodes traversed in the linked list. Otherwise, it returns -1.

>	2. int deallocate_mem (int process_id): deallocates the memory allocated to the process whose id is process_id. It returns 1, if successful, otherwise –1.

>	3. int fragment_count( ): returns the number of holes (fragments of sizes 1 or 2 units).

You will implement a separate Memory component for each memory allocation/deallocation technique. The request generation component generates allocation and deallocation requests. For allocation requests, the component specifies the process id of the process for which memory is requested as well as the number of memory units being requested. For this simulation, assume that memory is requested for each process only once. For deallocation requests, the component specifies the process id of the process whose memory has to be deallocated. For this simulation, assume that the entire memory allocated to a process is deallocated on a deallocation equest. You may generate these requests based on some specific criteria, e.g. at random or from a memory allocation/deallocation trace obtained from some source.

There are three performance parameters that your simulation should calculate for all four techniques: average number of external fragments, average allocation time in terms of the average number of nodes traversed in allocation, and the percentage of times an allocation request is denied.

Generate 10,000 requests using the request generation component, and for each request, invoke the appropriate function of the Memory component for each of the memory allocation/deallocation technique. After every request, update the three performance parameters for each of the techniques.

The statistics reporting component prints the value of the three parameters for all four techniques at the end.


**Twisted python linked list implementation for simulation**:

SEGMENT SPECIFICATION (2d list):

>	[PID, BASE_ADDR, LEN, PTR_INDEX]

or

>	[HOLE, BASE_ADDR, LEN, PTR_INDEX]

EXAMPLE 1:

>	mem = [ [7777, 0, 8, 1], [HOLE, 8, 4, 2], [8888, 12, 8, 0] ]

SNIPPETS:

	>>> alc = ['8888', 0, 3, 1]
	>>> mem2 = [['HOLE', 0, 128, None]]
	>>> mem2.insert(0, alc)
	>>> mem2
	[['8888', 0, 3, 1], ['HOLE', 0, 128, None]]
	>>> mem2 = [['HOLE', 0, 128, None]]
	>>> mem2[0][1] = 1
	>>> mem2[0][2] = 125
	>>> mem2.insert(0, alc)
	>>> mem2
	[['8888', 0, 3, 1], ['HOLE', 1, 125, None]]
	>>> alc = ['9999', 1, 5, 2]
	>>> mem2[1][1] = 2
	>>> mem2[1][2] = 120
	>>> mem2.insert(1, alc)
	>>> mem2
	[['8888', 0, 3, 1], ['9999', 1, 5, 2], ['HOLE', 2, 120, None]]
	>>> mem2[1][0] = 'HOLE'
	>>> mem2[1][1] = 1
	>>> mem2[1][2] = 5
	>>> mem2
	[['8888', 0, 3, 1], ['HOLE', 1, 5, 2], ['HOLE', 2, 120, None]]
	>>> 


