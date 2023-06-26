def isPossible(arr, n, m, curr_min):
    studentsRequired = 1
    curr_sum = 0

    for i in range(n):
 



        if (curr_sum + arr[i] > curr_min):

            studentsRequired += 1

            curr_sum = arr[i]


        else:
            curr_sum += arr[i]

        if (studentsRequired > m):
            return False
 
    return True
 
 
 
def findPages(arr, n, m):
 
 
    end = sum(arr)
    start = max(arr)
    while (start <= end):
        mid = (start + end) // 2
        if (isPossible(arr, n, m, mid)):

            result = mid
 
            end = mid - 1
 
        else:

            start = mid + 1
 
    return result
 
arr = [12, 34, 67, 90]
n = len(arr)
m = 2  
 
print(findPages(arr, n, m))