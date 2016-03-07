import random

def roll_snake_eyes():
	die_1 = random.randint(1, 6)
	die_2 = random.randint(1, 6)
	result = die_1 + die_2

	num_rolls = 1

	while result != 2:
		die_1 = random.randint(1, 6)
		die_2 = random.randint(1, 6)
		result = die_1 + die_2
		num_rolls += 1

	return num_rolls


# Main execution:

max_sims = int(raw_input('How many simulations? ==>'))

sims = 0
total = 0

# sim_results = []

while sims < max_sims:
	rolls = roll_snake_eyes()
	total = total + rolls
	# sim_results.append(rolls)
	sims = sims + 1

print '\n\n', max_sims, 'simulations were run.', 'Average number or rolls to get snake eyes is', str(total/max_sims)


