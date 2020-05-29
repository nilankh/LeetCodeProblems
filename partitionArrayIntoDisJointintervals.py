#915

def partitionArray(arr):
    n = len(arr)
    maxLeft = [None] * n
    minRight = [None] * n

    m = arr[0]
    for i in range(n):
        m = max(m, arr[i])
        maxLeft[i] = m
    #print(maxLeft)

    m = arr[-1]
    for i in range(n - 1, -1, -1):
        m = min(m, arr[i])
        minRight[i] = m
    #print(minRight)
    
    for i in range(1, n):
        if maxLeft[i - 1] <= minRight[i]:
            return i
    


arr = [int(x) for x in input().split()]
k = partitionArray(arr)
print(k)








