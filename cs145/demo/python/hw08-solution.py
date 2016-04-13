import random

from turtle import *

screen = Screen()

def max(list_to_process):
	
	max_val = list_to_process[0]
	for i in list_to_process:
		if i > max_val:
			max_val = i

	return max_val

def min(list_to_process):
	
	min_val = list_to_process[0]
	for i in list_to_process:
		if i < min_val:
			min_val = i

	return min_val

def avg(list_to_process):
	total = 0
	for i in list_to_process:
		total = total + i

	return total/len(list_to_process)


def plot_list(list_to_plot):
	WIDTH = 600.0
	scale = WIDTH/len(list_to_plot)
	tick = -300
	
	penup()
	setpos(-300, 0)
	pendown()

	for item in list_to_plot:
		if item < 20:
			dot_color = 'orange'
		elif item < 40:
			dot_color = 'black'
		elif item < 60:
			dot_color = 'blue'
		else:
			dot_color = 'green'


		color('gray')
		setpos(tick, item)
		color(dot_color)
		dot(10)

		color('black')

		tick += scale


	color('black')
	penup()
	setpos(0, -200)
	pendown()

	message = 'Minimum ==> ' + str(min(list_to_plot))
	write(message, move=False, align="left", font=("Arial", 14, "normal"))

	penup()
	setpos(0, -220)
	pendown()

	message = 'Maximum ==> ' + str(max(list_to_plot))
	write(message, move=False, align="left", font=("Arial", 14, "normal"))

	penup()
	setpos(0, -240)
	pendown()

	message = 'Average ==> ' + str(avg(list_to_plot))
	write(message, move=False, align="left", font=("Arial", 14, "normal"))


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

max_sims = int(raw_input('How many simulations? ==>'))

sims = 0
total = 0

sim_results = []

while sims < max_sims:
	rolls = roll_snake_eyes()
	total = total + rolls
	sim_results.append(rolls)
	sims = sims + 1

print '\n\n', max_sims, 'simulations were run.', 'Average number or rolls to get snake eyes is', str(total/max_sims)

plot_list(sim_results)

done()
