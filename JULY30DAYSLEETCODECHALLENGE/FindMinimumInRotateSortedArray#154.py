#154
#1st way
def minRotate1(arr):
    return min(arr)
    

def minRotate2(arr):
    minNum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minNum:
            minNum = arr[i]
    return minNum

def minRotate3(arr):
    # lets try with binary search as the aarray is sorted
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] < arr[r]:
            r = mid
        elif arr[mid] > arr[r]:
            l = mid + 1
        else:
            r -= 1
    return arr[l]
arr = [int(x) for x in input().split()]
#print(minRotate1(arr))
#print(minRotate2(arr))
print(minRotate3(arr))































