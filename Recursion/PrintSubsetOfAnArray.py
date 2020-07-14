#rough21
def printSubset(arr):
    printSubsetHelper(arr, [])
    
def printSubsetHelper(arr, lst):
    n = len(arr)
    if n == 0:
        for num in lst:
            print(num, end = ' ')
        print()
        return
    printSubsetHelper(arr[1:], lst)
    newList = lst.copy()
    newList.append(arr[0])
    printSubsetHelper(arr[1:], newList)
    return
n = int(input())
arr = [int(z) for z in input().split()]
printSubset(arr)
