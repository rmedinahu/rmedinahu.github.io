# mar-21-sim-malloc.py

import random

hole = ['HOLE', 0, 128]
first_fit_node_checks = 0
mem = [hole]

def allocate_mem_first_fit(pid, units):
	global mem, first_fit_node_checks
	# pseudocode:

	# search for first hole segment with capacity for units
	# insert new memory allocation segment at index of hole
	# update hole by decrementing its length by units

	insert_point = None
	mem_index = None
	for i in range(len(mem)):
		if mem[i][0] == 'HOLE' and mem[i][2] >= units: # segment type (hole or num)
			insert_point = mem[i][1]
			mem_index = i
			first_fit_node_checks = first_fit_node_checks + i
			break
	
	if insert_point is None:
		return -1  # Allocation fails exit and return fail flag.

	alc = [pid, insert_point, units]
	mem[mem_index][1] = mem[mem_index][1] + units # relocate hole start length of units
	mem[mem_index][2] = mem[mem_index][2] - units
	mem.insert(mem_index, alc)
	
	return 1

def deallocate_mem(pid):
	global mem

	for i in range(len(mem)):
		if mem[i][0] == pid:
			mem[i][0] = 'HOLE'
			return 1

	return -1

def print_debug():
	global mem
	print mem


def fragment_count():
	global mem
	total_frags = 0
	for i in mem:
		if i[0] == 'HOLE' and i[2] < 3:
			total_frags += 1

	return total_frags

"""***************************************************************"""
run = 1
while run <= 100:
	print 'alloc==>', allocate_mem_first_fit(run, random.randint(3, 10))
	if run % 3 == 0:
		debug = deallocate_mem(random.randint(1, run))
		if debug < 0:
			print "no deallocate!==>", mem
	
	run += 1

print_debug()
print 'NODE VISITS==>', first_fit_node_checks
print 'FRAGS==>', fragment_count()







