#932

    
    
def beautifulArray(n):
    arr = list(range(1, n + 1))
    def helper(arr):
        if len(arr) < 3:
            return arr
        even = arr[::2]
        odd = arr[1::2]

        return helper(even) + helper(odd)
    return helper(arr)#pehl call
    
    

n = int(input())
k = beautifulArray(n)
print(*k)
