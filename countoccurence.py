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

def last_occurrence(arr, low, high, n):
    if low > high:
        return -1

    mid = (low + high) // 2

    if n > arr[mid]:
        return last_occurrence(arr, mid + 1, high, n)
    elif n < arr[mid]:
        return last_occurrence(arr, low, mid - 1, n)
    else:
        if mid == high or arr[mid + 1] != arr[mid]:
            return mid
        else:
            return last_occurrence(arr, mid + 1, high, n)
def count(arr,low,high,n ):
    k=first_occurrence(arr,low,high,n)
    if k==-1:
        return 0
    else:
        m=last_occurrence(arr,k+1,high,n)
    if m==-1:
        return 1
    else:
        return m-k+1



arr=[2,2,2,3,3,4,5,5,6,7]
print(count(arr,0,len(arr),4))