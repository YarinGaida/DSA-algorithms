def quick_sort(arr, low=0, high=None):
    # Quick Sort Logic
    # Complexity: O(n log n) average case. 
    # (Worst case is O(n^2), but that's very rare with good pivot choice).
    
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 1. Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # 2. Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # This function takes the last element as pivot, places
    # the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to right
    
    pivot = arr[high] # Choosing the last element as pivot
    i = low - 1       # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap

    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1