from src.sorting.insertion_sort import insertion_sort
import random

try:
    user_input = input("Please enter the array's size: ")
    arr_length = int(user_input)
    
    if arr_length <= 0:
        print("Size must be a positive number.")
    else:
        # Generating random list based on user input size
        arr = [random.randint(1, 100) for _ in range(arr_length)]
        print(f"Before sorting: {arr}")
        
        insertion_sort(arr)
        print(f"After sorting:  {arr}")
        
except ValueError:
    print("Invalid input! Please enter a whole number.")