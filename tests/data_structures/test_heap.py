from src.data_structures.heap import MaxHeap
import random

try:
    heap = MaxHeap()
    user_input = input("Enter the length of the array (e.g., 10): ")
    len_of_array = int(user_input)
    
    if len_of_array <= 0:
        print("Size must be positive.")
    else:
        # Create random array
        arr = [random.randint(1, 100) for _ in range(len_of_array)]
        print(f"Original Array: {arr}")

        # Build Heap
        print("Building Max Heap...")
        heap.build_max_heap(arr)
        print(f"Heap Array:     {heap.heap}")
        
        print("Opening visualization window...")
        heap.plot_heap()
        
except ValueError:
    print("Invalid input! Please enter a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")