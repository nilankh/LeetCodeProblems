#275
def Hindex1(arr):
    #timecomplexity is O(n)
    n = len(citations)
    i = n - 1
    while(i >= 0):
        if citations[i] < n - i:
            break
        i -= 1
    return n - i - 1


def Hindex2(citations):
    n = len(citations)
    l = 0
    r = n - 1
    while(l <= r):
        mid = l + (r - l)//2
        if(citations[mid] < n - mid):
            l = mid + 1
        else:
            r = mid - 1
    return n - l
    


citations = [int(x) for x in input().split()]
#print(Hindex1(citations))
print(Hindex2(citations))
