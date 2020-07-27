#70
#recursive approach
def climbingStairs(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbingStairs(n - 2) + climbingStairs(n - 1)
    
#memoization
def climbingStairsM(n):
    dp = [0 for i in range( n + 1)]
    return helperM(n, dp)
def helperM(n, dp):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if dp[n] > 0:
        return dp[n]
    dp[n] = helperM(n - 1, dp) + helperM(n - 2, dp)
    return dp[n]


##iterative(ek baar leetcode ko dkho chota method v h_)
def climbingStairsI(n):
    if n == 1:
        return 1
    dp = [0 for i in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[ i - 2]
    return dp[n]
n = int(input())
#print(climbingStairs(n))
#print(climbingStairsM(n))
print(climbingStairsI(n))


























