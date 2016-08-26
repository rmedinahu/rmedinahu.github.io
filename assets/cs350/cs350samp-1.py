# cs350samp-1.py

def searchList(alist, query):
	for item in alist:
		if query == item:
			print 'found it!'


""" EXECUTION TIME """
seq = ('a', 'z', 'f', 'g', 'h', 'u', 'f', 'g', 'z')
searchList(seq, 'z')




