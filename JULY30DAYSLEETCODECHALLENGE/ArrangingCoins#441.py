#441
##FIRST METHOD
##def arrangeCoins(n):
##    if n < 2:
##        return n
##    else:
##        i = 1
##        count = 0
##        while count <= n:
##            count += i
##            i += 1
##        return i - 2

#2ND METHOD
##def arrangeCoins(n):
##    left = 0
##    right = n
##    while left <= right:
##        k = (right + left)//2
##        curr = k * (k + 1)//2
##        if curr == n:
##            return k
##        if n < curr:
##            right = k - 1
##        else:
##            left = k + 1
##    return right

#3rd method
import math
##def arrangeCoins(n):
##    k = (int)(math.sqrt(2*n))
##    sum = (int)(k*(k + 1)/2)
##    if sum > n: return k - 1
##    return k

#4th method(follow page no 52codebix)
def arrangeCoins(n):
##    return(int)((2*n+0.25)**0.5-0.5)
    return(int)(math.sqrt(2*n+0.25)-0.5)    
n = int(input())
print(arrangeCoins(n))




















