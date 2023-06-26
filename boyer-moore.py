def get_majority(arr):
    count = 1
    res = 0
    for i in range(1, len(arr)):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1

    count = 0
    for i in range(len(arr)):
        if arr[res] == arr[i]:
            count += 1
    
    if count > len(arr) // 2:
        return arr[res]
    else:
        return -1


arr = [1, 2, 3, 3, 3, 4, 5, 3, 3]
majority = get_majority(arr)
print(f"The majority element in the array {arr} is: {majority}")
