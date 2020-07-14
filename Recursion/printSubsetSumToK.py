#rough23
##def printSubsetHelper(arr, k, lst):
##    n = len(arr)
##    if n == 0:
##        return
##    if n == 1:
##        if arr[0] == k:
##            print(k, *lst)
##            return
##    printSubsetHelper(arr[:-1], k, lst)
##    printSubsetHelper(arr[:-1], k - arr[-1], [arr[-1]]+lst)
##    if arr[-1] == k:
##        print(k, *lst)
##
##def printSubset(arr, k):
##    printSubsetHelper(arr, k, [])
##n = int(input())
##arr = [int(z) for z in input().split()]
##k = int(input())
##printSubset(arr, k)

def printSubset(arr, k):
    #output = []
    printSubsetHelper(arr, 0, [], k)
def printSubsetHelper(arr, si, output, k):
    if si == len(arr):
        if k == 0:
            for i in output:
                print(i, end = ' ')
            print()
            return
        else:
            return
    newOutput = []
    newOutput = output.copy()
    newOutput.append(arr[si])
    printSubsetHelper(arr, si + 1, output, k)
    printSubsetHelper(arr, si + 1, newOutput, k - arr[si])
                      
n = int(input())
arr = [int(z) for z in input().split()]
k = int(input())
printSubset(arr, k)












