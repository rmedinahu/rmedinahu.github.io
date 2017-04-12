# hw_10_priority_queue.py

import unittest

class ClusterJob():
    def __init__(self, tag, rtime, lines):
        self.tag = tag
        self.runtime = rtime  # estimated runtime in seconds.
        self.code_lines = lines  # lines of code.

    def __str__(self):
        return self.tag + ': ' + str(self.load_factor())

    def __lt__(self, other_obj):
        return self.load_factor() < other_obj.load_factor()

    def load_factor(self):
        return self.runtime / float(self.code_lines)

class BinHeapList:
    """
    Binary heap as a priority queue using a list.

    subtree root = p
    left tree = p*2
    right tree = p*2+1
    parent of n = n//2 integer division
    """
    def __init__(self):
        """Creates a new, empty, binary heap as a list."""
        self.heap = [0]  # set first position to zero placeholder

    def insert(self, k):
        self.heap.append(k)  # add to end of list
        self.percUp(self.size())  # move new k up the tree 

    def getMin(self):
        return self.heap[1]

    def delMin(self):
        retval = self.heap[1]  # copy the front item.
        self.heap[1] = self.heap[-1]  # put last item first
        self.heap.pop() # clear last item (list decreases by 1)
        self.percDown(1)  # move first item down the tree
        return retval

    def percUp(self, p):
        """Maintains heap order property after insertion."""
        parent = self.parent(p)
        while parent > 0:
          if self.heap[p] < self.heap[parent]:
             tmp = self.heap[parent]
             self.heap[parent] = self.heap[p]
             self.heap[p] = tmp
          p = parent
          parent = self.parent(p)

    def percDown(self, p):
        """Maintains heap order property after deletion of root.
        Also note that the while loop processes the entire list
        """
        left = self.left(p)
        while left <= self.size():
            min_child = self.minChildIndex(p)
            if self.heap[p] > self.heap[min_child]:
                tmp = self.heap[p]
                self.heap[p] = self.heap[min_child]
                self.heap[min_child] = tmp
            p = min_child
            left = self.left(p)

    def minChildIndex(self, p):
        """Determines index of smaller of left and right values."""
        left, right = self.left(p), self.right(p)
        
        if right > self.size():  # right node does not exist
            return left
        
        elif self.heap[left] < self.heap[right]:
            return left
        
        return right

    def buildHeap(self, alist):
        i = len(alist) // 2  # start in middle of alist.
        self.heap = [0] + alist[:]  # initialize the heap list
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def size(self):
        return len(self.heap)-1

    def left(self, p):
        return p * 2

    def right(self, p):
        return p * 2 + 1

    def parent(self, p):
        return p // 2


class TestClusterJob(unittest.TestCase):
    """Unit tests for ClusterJob"""

    def test_cluster_job_compare_lt(self):
        a = ClusterJob('a', 5, 10)
        b = ClusterJob('b', 10, 100)
        self.assertEqual(a < b, True)

    def test_cluster_job_compare_gt(self):
        # write a test that verifies cluster jobs can be compared as a>b
        pass

    def test_heap_max(self):
        # write a test that verifies that the largest job is returned.
        pass


if __name__ == '__main__':
    unittest.main()

""" Sample setup for cluster jobs and heap.
    a = ClusterJob('a', 5, 10)
    b = ClusterJob('b', 10, 100)
    print a, b
    
    heap = BinHeapList()
    heap.insert(a)
    heap.insert(b)
"""





