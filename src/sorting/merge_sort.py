def MERGE(A, p, q, r):
    # 1. Create copies of the subarrays
    L = A[p:q+1]      # left subarray
    R = A[q+1:r+1]    # right subarray

    # 2. Add sentinel values (Infinity) to avoid boundary checks
    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0

    # 3. Merge loops - perfectly clean thanks to Infinity
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p=0, r=None):
    # Helper to allow calling merge_sort(arr) without arguments
    if r is None:
        r = len(A) - 1
        
    if p < r:
        q = (p + r) // 2  # Integer division (instead of math.floor)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        MERGE(A, p, q, r)