# feb-19.py

import random

# Definitions

def print_list(the_list):
	for item  in the_list:
		print item





nums = []
nums.append( random.randint(1, 20) )
nums.append( random.randint(1, 20) )
nums.append( random.randint(1, 20) )
nums.append( random.randint(1, 20) )
nums.append( random.randint(1, 20) )

nums[0] = nums[0] + 1
nums[1] = nums[1] + 1
nums[2] = nums[2] + 1
nums[3] = nums[3] + 1
nums[4] = nums[4] + 1

# Make LIST 1

random_length = random.randint(1, 20)

list1 = range(random_length)

random_length = random.randint(1, 20)
# list2 ...

random_length = random.randint(1, 20)
# list3 ...

user_input = raw_input('Size of your list:')
user_input = int(user_input)

mylist = range(user_input)
print mylist
#?????
print_list(mylist)





