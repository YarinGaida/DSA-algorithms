class Stack:
    """
    Stack implementation using a Python list.
    Follows LIFO principle (Last In, First Out).
    """
    def __init__(self):
        self.items = [] # "items" will hold all elements of the stack

    def push(self, value):
        """
        Adds an element to the top of the stack.
        Time Complexity: O(1)
        """
        self.items.append(value)

    def pop(self):
        """
        Removes and returns the top element.
        Returns None if the stack is empty.
        """
        if self.is_empty(): # calls to is_empty
            print("Stack is empty!")
            return None
        return self.items.pop()

    def peek(self):
        """
        Returns the top element without removing it.
        Useful for inspecting the stack's state.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Returns True if the stack contains no elements."""
        return len(self.items) == 0 # True if empty, False if not

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.items)