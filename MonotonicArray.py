##def isMonotonic(A):
##        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
##                all(A[i] >= A[i+1] for i in range(len(A) - 1)))
##
##
##n = int(input())
##A = [int(x) for x in input().split()]
##if(isMonotonic(A)):
##    print("true")
##else:
##    print("false")



##def isMonotonic(A):
##
##    return increasing(A) or decreasing(A)
##def increasing(A):
##    for i in range(len(A) - 1):
##        if(A[i] > A[i + 1]):
##            return False
##    return True
##
##def decreasing(A):
##    for i in range(len(A) - 1):
##        if(A[i] < A[i + 1]):
##            return False
##    return True
    

##n = int(input())
##A = [int(x) for x in input().split(',')]
##if(isMonotonic(A)):
##    print("true")
##else:
##    print("false")







def isMonotonic(A):
    increasing = decreasing = True
    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            increasing = False
        if A[i] < A[i+1]:
            decreasing = False
    return increasing or decreasing
n = int(input())
A = [int(x) for x in input().split(',')]
if(isMonotonic(A)):
    print("true")
else:
    print("false")


    

