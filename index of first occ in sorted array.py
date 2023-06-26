def first_occurrence(arr, low, high,n):
    if low > high:
        return -1

    mid = (low + high) // 2

    if n>arr[mid]:
        return first_occurrence(arr, mid+1, high,n)
    elif n<arr[mid]:
        return first_occurrence(arr, low, mid-1,n)
    else:
        if mid == 0 or arr[mid-1]!=arr[mid]:
            return mid
        else:
            return first_occurrence(arr,low,mid-1,n)

   


arr=[2,2,2,3,3,4,5,5,6,7]


print(first_occurrence(arr, 0,len(arr),2))

