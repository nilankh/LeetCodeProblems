#220
#page97
def containsDuplicate(arr, k, t):
    n = len(arr)
    if t == 0 and n == len(set(nums)):
        return False
    
    for i in range(len(arr)):
        for j in range(i + 1, i + 1 + k):
            if(j >= n):break
            if(abs(arr[i] - arr[j]) <= t):
                return True
    return False
    



arr = [int(x) for x in input().split()]
k = int(input())
t = int(input())
print(containsDuplicate(arr, k, t))


































