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
arr = [int(x) for x in input().split()]
#print(minRotate1(arr))
print(minRotate2(arr))










