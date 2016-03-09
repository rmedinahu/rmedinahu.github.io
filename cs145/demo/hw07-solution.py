# Solution for HW 07 
# 2016-03-09

import random

def roll_snake_eyes():
	die_1 = random.randint(1, 6)
	die_2 = random.randint(1, 6)
	num_rolls = 1
	result = die_1 + die_2

	while result != 2:
		die_1 = random.randint(1, 6)
		die_2 = random.randint(1, 6)
		num_rolls += 1
		result = die_1 + die_2

	return num_rolls


# MAIN EXECUTION:

sims_to_run = int(raw_input('How many simulations would you like to run? ==>'))

num_simulations_run = 0
total_of_all_rolls  = 0

# HW09 hint ==> Remember you need to keep track of each value returned by calling roll_snake_eyes() ...  a list will work perfectly!

while num_simulations_run < sims_to_run:
	num_rolls = roll_snake_eyes()
	total_of_all_rolls = total_of_all_rolls + num_rolls
	num_simulations_run = num_simulations_run + 1

	# remember to also store num_rolls in your ... list...

average = total_of_all_rolls/sims_to_run
print '\n\n', sims_to_run, 'simulations were run.'
print 'Average number of rolls to get snake eyes is ==>', average


