#35
def searchInsertPostion(arr, val):
    low = 0
    high = len(arr) - 1
    mid = 0
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] == val):
            return mid
        elif arr[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return low

#2nd method
def search(arr):
    if val in arr:
        return arr.index(val)
    else:
        arr.append(val)
        arr.sort()
        return(arr.index(val))
arr = [int(x) for x in input().split()]
val = int(input())
#k = searchInsertPostion(arr, val)
k = search(arr)
print(k)
