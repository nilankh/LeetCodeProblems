#153
def minRotated(arr):
    minVar = min(arr)
    for i in range(len(arr)):
        if arr[i] == minVar:
            return arr[i]
arr = [int(x) for x in input().split()]
k = minRotated(arr)
print(k)

