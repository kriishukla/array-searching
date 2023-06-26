def findMedian(A, B):
    n = len(A)
    m = len(B)
    if n >= m:
        return findMedian(B, A)  
 
    start = 0
    end = n
    real_mid_in_merged_array = (n + m + 1) // 2
 
    while start <= end:
        mid = (start + end) // 2
        left_A_size = mid
        left_B_size = real_mid_in_merged_array - mid
        left_A = A[left_A_size - 1] if left_A_size > 0 else float('-inf')
        left_B = B[left_B_size - 1] if left_B_size > 0 else float('-inf')
        right_A = A[left_A_size] if left_A_size < n else float('inf')
        right_B = B[left_B_size] if left_B_size < m else float('inf')
 
        if left_A <= right_B and left_B <= right_A:
            if (m + n) % 2 == 0:
                return (max(left_A, left_B) + min(right_A, right_B)) / 2.0
            return max(left_A, left_B)
        elif left_A > right_B:
            end = mid - 1
        else:
            start = mid + 1
    return 0.0

# Driver code
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print("Median of the two arrays are:")
print(findMedian(arr1, arr2))
