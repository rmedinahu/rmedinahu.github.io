# mar-4.py

from turtle import *
screen = Screen()

def draw_rect(w, h):
	lt(90);fd(h);lt(90);fd(w);lt(90);fd(h);lt(90);fd(w)


def plot_list(coords):
	color('black')
	WIDTH = 300
	scale = WIDTH/len(coords)
	tick = 0
	
	for item in coords:
		print pos()

		if item < 20:
			c = 'red'
			color('red')
		elif item < 40:
			c = 'blue'
			color('blue')
		elif item < 80:
			c = 'yellow'
			color('yellow')
		else:
			c = 'green'
			color('green')

		color('gray')
		setpos(tick, item)
		dot(10, c)

		tick += scale

coords = [8, 20, 50, 70, 20, 10, 90]
# plot_list(coords)
# draw_rect(200, 200)
done()