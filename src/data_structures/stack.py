class Stack:
  def __init__(self):
    self.items = [] # "items" will hold all elements of the stack

  def push(self,value): # add an element to the top
    self.items.append(value)

  def pop(self): # remove the top element
    if self.is_empty(): #calls to is_empty
      print("Stack is empty!")
      return None
    return self.items.pop()

  def peek(self): # look at the top element without removing it
    if self.is_empty():
      return None
    return self.items[-1]

  def is_empty(self):
      return len(self.items) == 0 # True if empty, False if not

  def size(self):
    return len(self.items)