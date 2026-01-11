from src.data_structures.linked_list import LinkedList


ll = LinkedList()
ll.append(4)
ll.append(10)
ll.append(11)
ll.append(2)

print("Original list:")
ll.display()

print("\nInserting 23 at index 2:")
ll.insert(23, 2)
ll.display()

print("\nDeleting 10:")
ll.delete(10)
ll.display()