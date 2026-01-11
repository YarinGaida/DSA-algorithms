import random
from src.sorting.quick_sort import quick_sort

try:
    print("--- Running Test for Quick Sort ---")
    user_input = input("Please enter the array's size: ")
    arr_length = int(user_input)
    
    if arr_length <= 0:
        print("Size must be a positive number.")
    else:
        # Create random list
        arr = [random.randint(1, 100) for _ in range(arr_length)]
        print(f"Before sorting: {arr}")
        
        # Run the algorithm
        # Note: Quick Sort works in-place (changes the original list)
        quick_sort(arr)
        
        print(f"After sorting:  {arr}")
        
except ValueError:
    print("Invalid input! Please enter a whole number.")