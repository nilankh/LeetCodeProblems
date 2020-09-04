#219
#95page
##TLE APPROACH
##def containsDuplicate(arr, k):
##    for i in range(len(arr)):
##        for j in range(i + 1, len(arr)):
##            if arr[i] == arr[j]:
##                t = abs(i - j)
##                if t <= k:
##                    return True
##    return False
def containsDuplicate(arr, k):
    d = {}
    for i in range(len(arr)):
        #print("I", i)
        if arr[i] in d:
            prevIndex = d[arr[i]]
            #print("prevIndex",prevIndex)
            latest = abs(i - prevIndex)
            
            if latest <= k:
                return True
            else:
                d[arr[i]] = i
        else:
            d[arr[i]] = i
            #print("D",d)
    #print(d)
    return False


arr = [int(k) for k in input().split()]
k = int(input())
print(containsDuplicate(arr, k))





















































