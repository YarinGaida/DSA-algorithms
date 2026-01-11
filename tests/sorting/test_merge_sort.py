import random
from src.sorting.merge_sort import merge_sort

try:
    print("--- Running Test for Merge Sort ---")
    user_input = input("Please enter the array's size: ")
    arr_length = int(user_input)
    
    if arr_length <= 0:
        print("Size must be a positive number.")
    else:
        # Create random list
        arr = [random.randint(1, 100) for _ in range(arr_length)]
        print(f"Before sorting: {arr}")
        
        # p = 0
        # r = len(arr) - 1
        merge_sort(arr, 0, len(arr) - 1)
        
        print(f"After sorting:  {arr}")
        
except ValueError:
    print("Invalid input! Please enter a whole number.")