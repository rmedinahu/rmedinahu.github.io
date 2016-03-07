# mar-4.py

from turtle import *
import random
screen = Screen()

def generate_random_nums(n):
	random_nums = []
	for i in range(n):
		random_num = random.randint(40, 100)
		random_nums.append(random_num)

	return random_nums

def draw_rect(w, h):
	lt(90)
	fd(h)
	lt(90)
	fd(w)
	lt(90)
	fd(h)
	lt(90)
	fd(w)

def plot_list(list_to_plot):
	WIDTH = 300.0
	scale = WIDTH/len(list_to_plot)
	tick = 0
	
	for item in list_to_plot:
		if item > 89:
			dot_color = 'green'
		elif item > 79:
			dot_color = 'orange'
		elif item > 69:
			dot_color = 'blue'
		elif item > 59:
			dot_color = 'yellow'
		else:
			dot_color = 'red'

		color('gray')
		setpos(tick, item)
		dot(10, dot_color)

		tick += scale

# Main execution
list_plot = generate_random_nums(40)
plot_list(list_plot)

# draw_rect(200, 200)
done()