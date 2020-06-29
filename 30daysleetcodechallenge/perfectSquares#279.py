#279
#first method
import sys
def perfectSquares(n):
    dp = [0] *(n + 1)
    for x in range(1, n+1):
        min_val = x
        y, sq = 1, 1
        while sq <= x:
            min_val = min(min_val, 1 + dp[x - sq])
            y += 1
            sq = y * y
        dp[x] = min_val
    return dp[n]
            
#2nd method tle error        
def perfectSquares2(n):
    return rec(n)
def rec(n):
    if n < 0:
        return sys.maxsize
    if n == 0:
        return 0
    mini = n
    for i in range(1, n + 1):
        temp = i * i
        if temp <= n:
            mini = min(rec(n - (i * i)), mini)
        else:
            break
    return mini + 1

n = int(input())
print(perfectSquares2(n))


















