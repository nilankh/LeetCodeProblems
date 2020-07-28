import math, sys
def minSquares(n):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        currAns = 1 + minSquares(n - (i ** 2))
        ans = min(ans, currAns)
    return ans

def minSquaresRM(n, dp):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        newCheckValue = n - (i ** 2)
        if dp[newCheckValue] == -1:
            smallAns = minSquaresRM(newCheckValue, dp)
            dp[newCheckValue] = smallAns;
            currAns = 1 + smallAns
            
        else:
            currAns = 1 + dp[newCheckValue]
        ans = min(ans, currAns)
    return ans

n = int(input())
dp = [-1 for i in range(n + 1)]
ans = minSquaresRM(n, dp)
##ans = minSquares(n)
print(ans)





























