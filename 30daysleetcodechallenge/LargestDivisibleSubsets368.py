def largestDivisibleSubset(arr):
    arr.sort()
    res = []
    helper(arr, 0, res, 1)
    return res
def helper(arr, index, curr, prev):
    if len(curr) > 
arr = [int(x) for x in input().split()]
largestDivisibleSubset(arr)
