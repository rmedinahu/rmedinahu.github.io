# preassess-20170310.py

import unittest, random

"""Remove the pass statement then implement the following python function so 
that it swaps the values in the arguments first and last. 

Returns the variable named first (after it is swapped!).
"""
def swap(first, last):
	pass


"""Implement the following python function so that it swaps the first and last 
values from the list argument. 

Return the variable named alist after you have swapped the values.
"""
def swap_first_last(alist):
	return alist


"""Remove the pass statement then implement the following python function so 
that it locates the smallest number in the list argument. 

Return the smallest value found. Please do not use python's min() function.
"""
def find_min(alist):
	pass


"""Remove the pass statement then implement the following python function so 
that it locates the largest number given in the list argument. 

Return the largest value found. Please do not use python's max() function.
"""
def find_max(alist):
	pass


"""Remove the pass statement then implement the following python function so that
it reports the frequency of the argument, target, within the list called alist. 

Return the frequency. Please do not use python's count() function.
"""
def find_frequency(alist, target):
	pass


"""Remove the pass statement then implement the following python function so 
that it reverses the order of the elements in the argument alist.

Returns the reversed alist. Please do not use python's reverse() function.
"""
def reverse_list(alist):
    pass


"""Remove the pass statement then implement the following python function so 
that it builds a new word by substituting each number in the given list 
argument according to the rules specified below.

Returns the new word as a string.

Here are the substitution rules:  

[103, 117, 105, 100, 111]
FOR EACH ITEM in LIST WRITE ONE CHARACTER TO A STRING USING THE FOLLOWING RULES:
    ITEM < 101 write character 'd'
    100 < ITEM < 104 is 'g'
    103 < ITEM < 107 is 'i'
    106 < ITEM < 112 is 'o'
    111 < ITEM < 118 is 'u'
"""
def substitute_sequence(coded_nums):
    pass


"""Remove the pass statement then implement the following python function so 
that it computes the average of all the values given list argument.

Returns the average using floating point precision.
"""
def median_range(data_points):
    pass


"""Remove the pass statement then implement the following python function so 
that it builds a new string by reading every other character from the given 
argument, message.

Returns the 'deciphered' message as a string.

3gvupiqdeoywzaqshh7ewrxe


The deciphered text should begin with the second letter of the message and 
include every OTHER subsequent letter after that.
"""
def decipher_sequence(message):
    pass


"""Remove the pass statement then implement the following python function so
that it returns True or False if the given string argument is a palindrome. A 
palindrome is a word that is same whether spelled forward or backward.

E.g. 'racecar' is a palindrome while 'spot' is not.

Returns true or false.
"""
def is_palindrome(word):
    pass


################################################################################
################################################################################
################################################################################
################################################################################
######         Unit Tests. Do not modify source below.                    ######
################################################################################
################################################################################
################################################################################
################################################################################

data_a = [457, 947, 204, 571, 191, 266, 823, 326, 979, 944, 655, 452, 727, 943, 
    850, 774, 611, 393, 851, 109, 784, 765, 418, 248, 295, 239, 275, 114, 329]
data_b = [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 
    1, 1, 1, 1, 1, 0]

class PreassessTestMethods(unittest.TestCase):
    
    def test_swap(self):
        result = swap('golden', 'shores')
        self.assertEqual(result, 'shores')


    def test_swap_first_Last(self):
        result = swap_first_last(range(2, 100, 3))
        self.assertEqual(result[0], 98)
        self.assertEqual(result[-1], 2)

    def test_find_min(self):
        result = find_min(data_a[:])
        self.assertEqual(result, 109)


    def test_find_max(self):
        result = find_max(data_a[:])
        self.assertEqual(result, 979)


    def test_find_frequency(self):
        result = find_frequency(data_b[:], 1)
        self.assertEqual(result, 17)


    def test_reverse_list(self):
        result = reverse_list(['U', 'C', 'Z', 'i', 'S', 'k'])
        self.assertEqual(result, ['k', 'S', 'i', 'Z', 'C', 'U'])


    def test_substitute_sequence(self):
        result = substitute_sequence([103, 117, 105, 100, 111])
        self.assertEqual(result, 'guido')


    def test_median_range(self):
        result = median_range(data_a[:])
        self.assertEqual(result, 535.8620689655172)


    def test_decipher_sequence(self):
        result = decipher_sequence('3gvupiqdeoywzaqshh7ewrxe')
        self.assertEqual(result, 'guidowashere')


    def test_is_palindrome(self):
        result = is_palindrome('racecar')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()