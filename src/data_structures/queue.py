from collections import deque

class Queue:
    def __init__(self):
        # I used 'deque' because popping from the start of a standard list is slow (O(n)).
        # deque allows O(1) for adding/removing from both ends.
        self.items = deque()

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        self.items.append(value)

    def dequeue(self):
        """Remove the first element from the queue (FIFO)."""
        if self.is_empty():
            return None
        return self.items.popleft() # 'popleft' is optimized for queues

    def peek(self):
        """Look at the front element without removing it."""
        if self.is_empty():
            return None
        return self.items[0] # Access the first element

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Queue({list(self.items)})"