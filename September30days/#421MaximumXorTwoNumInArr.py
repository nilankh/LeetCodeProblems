#time complexity O(n^2)

def maximumXOR(arr):
    maxi = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            maxi = max(maxi, arr[i] ^ arr[j])
    return maxi



arr = [int(x) for x in input().split()]
print(maximumXOR(arr))












