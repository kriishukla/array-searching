def bin_search(arr, start, end, n):
    if start > end:
        return -1

    mid = (start + end) // 2
    if arr[mid] == n:
        return mid
    elif arr[mid] < n:
        return bin_search(arr, mid + 1, end, n)
    else:
        return bin_search(arr, start, mid - 1, n)

arr = [2, 3, 4, 5, 6, 7, 8]
print(bin_search(arr, 0, len(arr) - 1, 8))
