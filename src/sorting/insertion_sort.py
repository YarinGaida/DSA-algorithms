import random

def insertion_sort(arr):
    # Insertion Sort Logic
    # Complexity: O(n^2) - Good for small arrays or nearly sorted data
    
    # starts at the second index (assuming first is sorted)
    for i in range(1, len(arr)): 
        key = arr[i] # key is the element we want to insert correctly
        j = i - 1
        
        # Shift elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # swap/shift right
            j = j - 1
            
        arr[j + 1] = key # Place key at after the element just smaller than it