def partition(A, low, high):
    # Choose the last element as pivot
    pivot = A[high]
    i = low - 1  # place for the smaller element i=-1

    # Rearrange elements around the pivot
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]  # swap smaller element to the left side

    # Place pivot in its correct position
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1  # return the pivot index


def quick_sort(A, low, high):
    if low < high:
        # Partition the array
        pi = partition(A, low, high)

        # Recursively sort elements before and after the pivot
        quick_sort(A, low, pi - 1)   # left side
        quick_sort(A, pi + 1, high)  # right side


# Example usage
A = [7, 2, 1, 6, 8, 5, 3, 4] # [1, 2, 3 |, 4, | 8, 5, 7, 6] => [2,1,3,4,7,6,8]
quick_sort(A, 0, len(A) - 1)
print("Sorted array:", A)