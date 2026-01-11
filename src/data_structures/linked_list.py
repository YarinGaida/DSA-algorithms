from typing import Any, Optional

class Node:
    """A single node in the linked list containing data and a reference to the next node."""
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['Node'] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, value: Any) -> None:
        """Adds a new node containing value to the end of the list."""
        new_node = Node(value)
        
        # If the list is empty, just set the head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node

    def insert(self, value: Any, position: int) -> None:
        """Inserts a new node at the specified position (0-indexed)."""
        new_node = Node(value)

        # Case 1: Inserting at the beginning
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Case 2: Traversing to find the split point
        current = self.head
        prev = None
        count = 0

        while current and count < position:
            prev = current
            current = current.next
            count += 1

        # Validation: Did we go out of bounds?
        if count < position:
            raise IndexError("Position out of bounds.")

        # Stitching the new node in
        prev.next = new_node
        new_node.next = current

    def delete(self, key: Any) -> None:
        """Deletes the first node containing the specified key."""
        current = self.head

        # Case 1: Head itself holds the key
        if current and current.value == key:
            self.head = current.next
            current = None # Help GC clean up
            return

        # Case 2: Search for the key deeper in the list
        prev = None
        while current and current.value != key:
            prev = current
            current = current.next

        # Case 3: Key not found
        if not current:
            return

        # Unlink the node from the list
        prev.next = current.next
        current = None

    def display(self) -> None:
        """Prints the list in a readable format (e.g., head -> 1 -> 2 -> None)."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        
        # Joining list is cleaner than printing inside the loop
        print("head -> " + " -> ".join(elements) + " -> None")