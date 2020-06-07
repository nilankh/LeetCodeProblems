def queueReconstruction(arr):
    result = []
    arr.sort(key = lambda x: (-x[0],x[1]))
    for x in arr:
        print("x",x)
        result.insert(x[1],x)
    return result

s=input().split()
n,m=int(s[0]),int(s[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]
#row_sum(arr)
print(queueReconstruction(arr))

