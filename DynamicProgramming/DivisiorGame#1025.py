#page no 73-75
#time complexity is O(2^n)
##def canWin(n):
##    if n <= 1:
##        return False
##    for x in range(1,n):
##        if(n % x == 0):
##            if not canWin(n - x):
##                return True
##    return False
##
##n = int(input())
##print(canWin(n))



#Memoization Method
#O(N^2)
'''
def canWinRM(n, cache):
    if n <= 1:
        return False
    if cache[n] is not None:
        return cache[n]
##    for x in range(1, n + 1):
    for x in range(1, n//2 + 1):
        if n % x == 0:
            if not canWinRM(n - x, cache):
                cache[n] = True
                return True
    cache[n] = False
    return False
n = int(input())
cache = [None for i in range(n + 1)]
print(canWinRM(n, cache))'''

#3rd method mathmatical approach
def canWinM(n):
    return n % 2 == 0
n = int(input())
print(canWinM(n))























