import unittest


class EmptyStack(Exception):
    """Custom Exception"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
          self._element = element               # reference to user's element
          self._next = next                     # reference to next node

    #------------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None                       # reference to the head node
        self._size = 0                          # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def push_seq(self, seq):
        """Iteratively push each element in seq to stack."""
        pass

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        return self._head._element              # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        answer = self._head._element
        self._head = self._head._next           # bypass the former top node
        self._size -= 1
        return answer

    def as_string(self):
        """Recursively build a string containing each element of the stack without modifying the stack.
        
        Returns the string beginning with the top element on one line separated by spaces.
        """
        pass


class TestLinkedStackMethods(unittest.TestCase):
    """Unit tests for LinkedStack"""

    def test_init(self):
        stack = LinkedStack()
        self.assertEqual(len(stack), 0)

    def test_is_empty(self):
        pass
    
    def test_push(self):
        pass

    def test_push_seq(self):
        pass

    def test_top(self):
        pass
    
    def test_top_exception(self):
        stack = LinkedStack()
        with self.assertRaises(EmptyStack):
            stack.top()
    
    def test_pop(self):
        pass

    def test_pop_exception(self):
        """Tests whether pop correctly raises EmptyStack exception."""

    def test_as_string(self):
        """Tests that as_string correctly lists the contents of the stack."""
        pass

"""Run the unit tests on invocation of this file with python interpreter.

> python <name of this file>.py
"""
if __name__ == '__main__':
    unittest.main()



