#448

def DisappearedArray(arr):
    s1 = set(range(1, len(arr) + 1))
    #print(s1)
    s2 = set(arr)
    #print(s2)
    return list(s1 - s2)
    

n = int(input())
arr = [int(x) for x in input().split()]
k = DisappearedArray(arr)
print(k)

    
    
        
        
