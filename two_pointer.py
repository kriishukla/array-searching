def two_pointer(arr, n):
    low = 0
    high = len(arr) - 1

    while low < high:
        if arr[low] + arr[high] == n:
            print(low, high)
            return  
        elif arr[low] + arr[high] > n:
            high -= 1
        else:
            low += 1

arr = [1, 2, 3, 4, 5]
target = 7
two_pointer(arr, target)
