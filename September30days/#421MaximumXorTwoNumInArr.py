#time complexity O(n^2)

##def maximumXOR(arr):
##    maxi = 0
##    for i in range(len(arr) - 1):
##        for j in range(i + 1, len(arr)):
##            maxi = max(maxi, arr[i] ^ arr[j])
##    return maxi


def maximumXOR(arr):
    result = 0
    for i in reversed(range(32)):
        result <<= 1
        prefixes = set()
        for n in arr:
            prefixes.add(n >> i)
        for p in prefixes:
            if(result | 1) ^ p in prefixes:
                result += 1
                break
    return result
arr = [int(x) for x in input().split()]
print(maximumXOR(arr))












