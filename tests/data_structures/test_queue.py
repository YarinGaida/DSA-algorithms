from src.data_structures.queue import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)          # Queue([1, 2, 3])

print(q.dequeue()) # 1
print(q.peek())    # 2

print(q.size())    # 2