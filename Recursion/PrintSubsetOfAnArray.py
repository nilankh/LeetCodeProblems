def printSubset(arr):
    printSubsetHelper(arr, [])
    


n = int(input())
arr = [int(z) for z in input().split()]
printSubset(arr)
