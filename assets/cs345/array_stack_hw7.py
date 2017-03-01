import unittest


class EmptyStack(Exception):
    """Custom Exception"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise EmptyStack('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise EmptyStack('Stack is empty')
    return self._data.pop()               # remove last item from list

  def get_data(self):
        """returns the underlying data structure for the stack."""
        pass

  def push_seq(self, seq):
      """Iteratively push each element in seq to stack."""
      pass

  def as_string(self, s):
      """Recursively build a string containing each element of the stack without modifying the stack.
      
      The final string should contain each element of the stack separated by a space. This time though 
      the BOTTOM of the stack should be first and the TOP of the stack should be last.
      """
      pass


class TestArrayStackMethods(unittest.TestCase):
    """Unit tests for ArrayStack"""

    def test_init(self):
        pass

    def test_is_empty(self):
        pass
    
    def test_push(self):
        pass

    def test_push_seq(self):
        pass

    def test_top(self):
        pass
    
    def test_top_exception(self):
      """Tests whether top correctly raises EmptyStack exception."""
        pass
    
    def test_pop(self):
        pass

    def test_get_data(self):
        pass

    def test_pop_exception(self):
        """Tests whether pop correctly raises EmptyStack exception."""

    def test_as_string(self):
        """Tests that as_string correctly lists the contents of the stack in indicated order (bottom -> top)."""
        pass



"""Run the unit tests on invocation of this file with python interpreter.

> python <name of this file>.py
"""
if __name__ == '__main__':
    unittest.main()