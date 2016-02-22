# feb-22.py

# Definitions

def star_gazer(n):
	stars = ''

	# Loop n times each time add one asterisk to stars.
	for i in range(n):
		stars = stars + '*'

	print stars

# Main execution begins:
user_input = raw_input("Enter stars you would like to gaze upon: ")
user_input = int(user_input)

star_gazer(user_input)



