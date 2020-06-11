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



arr = [int(x) for x in input().split()]
val = int(input())
k = searchInsertPostion(arr, val)
print(k)
