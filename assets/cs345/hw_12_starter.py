"""
hw_12_starter.py
A starter file for a simple hash table class. Use
for Homework 12 Apr 26 2017
"""

class HashSetTbl:
    
    def __init__(self):
        """ constructor creates a 10 empty buckets 
        each bucket contains zero or more unique values.
        def. This class maintains a set property (all unique values)
        """
        self.bucket_list = [ [] ] * 10 

    def __getitem__(self, v):
        """override retrieval to support syntax: tblobject['red'] 
        should return the value v in table
        if v not found in table, raise KeyError
        Must use the hash value of v THEN sequential search of bucket
        at index[h(v)]
        """
        pass

    def insert(self, v):
        """assignment to support syntax: tblobject.add('blue')
        should add the value v to proper bucket in table IF it does 
        not already exist.
        """
        pass

    def __iter__(self):
        """ implement generator to allow looping over entire contents
        of the set.
        """
        pass

    def __len__(self):
        """ returns the total number of assigned values in table."""
        pass
    
    def bucket_dump(self):
        """ prints a snapshot of the bucket list to the screen. Example:
            [0]: 'a', 'tree', 'mouse'
            [1]: 'red'
            ...
            [9]: 'top', 'bottom'
        """
        pass

    def hash_func(self, v):
        """
        a. computes a hash code for v using python hash() function
        b. compresses hash code relative to size of bucket list.
        returns the compression value
        """
        pass


if __name__ == '__main__':

    h = HashSetTbl()
    

