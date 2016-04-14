"""
read_seq => 5, 20, 3, 40, 1, 0

fcfs ==> iterate from beginning to end.

sdf ==>
	start = read_seq[0]
	simulated_disk = [0, 1, 3, 5, 20, 40] (really just seq but sorted to simulate ordered cylinders)
	start_index = simulated_disk.index(start)

	begin first read at simulated_disk[start_index]

	for every read clear the value at index

elevator ==>
	start = read_seq[0]
	simulated_disk = [0, 1, 3, 5, 20, 40] (really just seq but sorted to simulate ordered cylinders)
	start_index = simulated_disk.index(start)

	begin first read at simulated_disk[start_index]

	for every read clear the value at index
"""

import random

DISK_SIZE = 1000

def get_rand_cylinder(ceiling, sequence):
	cylinder_num = random.randint(0, ceiling)
	while True:
		if cylinder_num not in sequence:
			return cylinder_num

		cylinder_num = random.randint(0, ceiling)

def populate_sequence(seq_len, cylinder_range):
	read_seq = [None] * seq_len
	for i in range(seq_len):
		read_seq[i] = get_rand_cylinder(cylinder_range, read_seq)
	return read_seq

def build_simulated_disk(size, seq):
	simulated_disk = [None] * size
	for i in seq:
		simulated_disk[i] = i
	return simulated_disk

def scan_lt(seq, head):
	scanner = head - 1
	while scanner >= 0:
		if seq[scanner]:
			return scanner 
		scanner -= 1
	return -1

def scan_rt(seq, head):
	scanner = head + 1
	while scanner < len(seq):
		if seq[scanner]:
			return scanner 
		scanner += 1
	return -1

def fcfs(seq):
	dist = 0
	for i in range(len(seq)- 1):
		a = seq[i]
		b = seq[i+1]
		dist += abs(a - b)
	return dist

def sdf(seq):
	global DISK_SIZE
	dist = 0
	sim_disk = build_simulated_disk(DISK_SIZE, seq)
	read_head = seq[0]
	
	left = scan_lt(sim_disk, read_head)
	right = scan_rt(sim_disk, read_head)

	while (left + right) != -2: # no cylinders left to read on either side.
		d_lt = abs(left - read_head)
		d_rt = abs(right - read_head)

		if left < 1 and right > 0: 		# nothing on the left, moving to cylinder on right
			dist += d_rt
			sim_disk[read_head] = None 	# Clear previous read then update read_head
			read_head = right

		elif right < 1 and left > 0: 	# nothing on the right, moving to cylinder on left
			dist += d_lt
			sim_disk[read_head] = None 	# Clear previous read then update read_head
			read_head = left		
		
		elif d_lt < d_rt: # moving to cylinder on left
			dist += d_lt
			sim_disk[read_head] = None 	# Clear previous read then update read_head
			read_head = left		

		else: # moving to cylinder on right
			dist += d_rt
			sim_disk[read_head] = None 	# Clear previous read then update read_head
			read_head = right	

		left = scan_lt(sim_disk, read_head)
		right = scan_rt(sim_disk, read_head)

	return dist

def elevator(seq):
	global DISK_SIZE
	dist = 0
	sim_disk = build_simulated_disk(DISK_SIZE, seq)
	read_head = seq[0]
	
	left = scan_lt(sim_disk, read_head)
	right = scan_rt(sim_disk, read_head)

	going_up = True

	while (left + right) != -2:
		if going_up:
			right = scan_rt(sim_disk, read_head)
			if right < 0:
				going_up = False
			else:
				dist += abs(sim_disk[right] - sim_disk[read_head])
				sim_disk[read_head] = None
				read_head = right		 
		else:
			left = scan_lt(sim_disk, read_head)
			if left < 0:
				going_up = True
			else:
				dist += abs(sim_disk[left] - sim_disk[read_head])
				sim_disk[read_head] = None
				read_head = left

	return dist

# Main...


read_sequence = populate_sequence(10, DISK_SIZE)

"""
	Test sequence from textbook. Uncomment next line to use test sequence.
	Expected output is as follows:
		FCFS = 111, SDF = 61, ELEVATOR = 60
"""
read_sequence = [11, 1, 36, 16, 34, 9, 12] 

print '\nRead sequence ==> ', read_sequence
print 'Initial read_head position ==>', read_sequence[0]

print '\nFCFS Cost ==>', fcfs(read_sequence)
print 'SDF  Cost ==>', sdf(read_sequence)
print 'ELVT Cost ==>', elevator(read_sequence)



