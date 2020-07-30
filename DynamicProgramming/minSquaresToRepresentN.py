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

#time complexity is nrootn.
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

#time complexity nrootn sp = O(N)
def minSquaresI(n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        ans = sys.maxsize
        root = int(math.sqrt(i))
        for j in range(1, root + 1):
            currAns = 1 + dp[i - (j ** 2)]
            ans = min(ans, currAns)
            #print(dp)
        dp[i] = ans
    return dp[n]
        
    
n = int(input())
#dp = [-1 for i in range(n + 1)]
#ans = minSquaresRM(n, dp)
##ans = minSquares(n)
ans = minSquaresI(n)
print(ans)



def long(string):
    if len(string) == 0:
        return ""
    hum = string[0]
    for i in range(1, len(string)):
        while hm != string[i][:len(hum)]:
            hum = hum[:-1]
            if hum == "":
                return ""
    return hm

























