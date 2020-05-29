#442

from collections import Counter 
def findAllDuplicates(arr):
    d = Counter(arr)
    arr.clear()
    for i in d:
        if d[i] > 1:
            arr.append(i)
    return arr
    

    
arr = [int(x) for x in input().split()]
k = findAllDuplicates(arr)
print(*k)
