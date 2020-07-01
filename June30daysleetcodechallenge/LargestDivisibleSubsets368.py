def largestDivisibleSubset(arr):
    if len(arr) == 0:
        return []
    arr.sort()
    result = [[num] for num in arr]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] % arr[j] == 0 and len(result[i]) < len(result[j]) + 1:
                result[i] = result[j] + [arr[i]]
    return max(result, key = len)
     
arr = [int(x) for x in input().split()]
k = largestDivisibleSubset(arr)
print(*k)
