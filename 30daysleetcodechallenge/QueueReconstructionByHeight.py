def queueReconstruction(arr):
    result = []
    arr.sort(key = lambda x: (-x[0],x[1]))
    #print(arr)
    for x in arr:
        #print("x",x)
        #print("x1",x[1])
        result.insert(x[1],x)
        #ye jo x h it means sit is inserting at x postition
        #print("result", result)
    return result

s=input().split()
n,m=int(s[0]),int(s[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]
#row_sum(arr)
print(queueReconstruction(arr))



'''
>>> arr = [ [3, 4],[5, 3], [3, 0], [5, 2], [2, 7]]
>>> arr.sort(key = lambda x: -x[0])
>>> arr
[[5, 3], [5, 2], [3, 4], [3, 0], [2, 7]]
>>> arr = [ [3, 4],[5, 3], [3, 0], [5, 2], [2, 7]]
>>> arr.sort(key = lambda x:(-x[0],x[1]))
>>> arr
[[5, 2], [5, 3], [3, 0], [3, 4], [2, 7]]'''
