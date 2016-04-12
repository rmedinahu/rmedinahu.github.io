

import random

def get_rand_cylinder(limit, sequence):
	cyl = random.randint(0, limit)
	
	while True:
		if cyl not in sequence:
			return cyl


def populate_sequence(seq_len, cyl_range):
	seq = [None] * cyl_range

	for i in range(seq_len):
		randindex = get_rand_cylinder(cyl_range, seq)
		seq[randindex] = True

	return seq

def fcfs(seq):
	dist = 0
	for i in range(len(seq)- 1):
		if seq[i]:
			dist += abs(seq[i] - seq[i+1])

	return dist


def sdf(seq):
	dist = 0


def elevator(seq):
	dist = 0
	direction = 0


# Main...


seq = populate_sequence(10, 999)
print fcfs(seq)



