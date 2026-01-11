def merge_sort(arr):
    # Merge Sort Logic
    # Complexity: O(n log n) - Very fast for large datasets
    
    # Base case: A list of 0 or 1 elements is already sorted
    if len(arr) > 1:
        
        # 1. DIVIDE: Find the middle and split into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls to sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # 2. CONQUER (Merge): Merge the sorted halves back into arr
        i = 0 # pointer for left_half
        j = 0 # pointer for right_half
        k = 0 # pointer for main arr

        # Compare elements from both halves and overwrite arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 3. CLEANUP: If any elements are left in either half, add them
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1