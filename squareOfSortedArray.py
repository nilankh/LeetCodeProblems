def Sorted(arr):
    l = len(arr)
    li = []
    for i in range(l):
        li.append(arr[i]**2)
    li.sort()
    for i in range(len(li)):
        arr[i] = li[i]
    return arr

def sortedSquares(arr):
    return sorted(x*x for x in arr)

n = int(input())
arr = [int(x) for x in input().split()]
#k = Sorted(arr)
k = sortedSquares(arr)
print(*k)
