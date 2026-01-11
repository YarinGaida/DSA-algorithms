from src.data_structures.stack import Stack

S = Stack() # empty stack is created
S.push(10)
S.push(9)
print(S.items)
print("Popped:", S.pop())
print(S.items)