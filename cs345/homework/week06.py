# week06.py

# This Python file uses the following encoding: utf-8

import os


bar = '├── '
bardir = '└── '
space = '    '

def list_files(p=None, level=0):
	if os.path.isfile(p):
		print space * level + bar + os.path.basename(p)
		return
	print space * level + bardir + os.path.basename(p)
	for i in os.listdir(p):
	list_files(os.path.join(p, i), level + 1)

if __name__ == '__main__':
	os.chdir('/Users/rmedina/pythonweb/ggv-py/pretests')
	list_files(os.getcwd(), 0)