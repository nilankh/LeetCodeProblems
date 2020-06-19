#275
def Hindex(arr):
    n = len(citations)
    i = n - 1
    while(i >= 0):
        if citations[i] < n - i:
            break
        i -= 1
    return n - i - 1
    


citations = [int(x) for x in input().split()]
print(Hindex(citations))
