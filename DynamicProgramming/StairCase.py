def FindStep(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    else:
        return FindStep(n-3)+FindStep(n-2)+FindStep(n-1)

#memoization method
def findStepM(n):
    dp = [0 for i in range(n + 1)]
    return helper(n, dp)
def helper(n, dp):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if dp[n] > 0:
        return dp[n]
    dp[n] = helper(n - 3, dp) + helper(n - 2, dp) + helper(n - 1, dp)
    return dp[n]
n=int(input())
##print(FindStep(n))
print(findStepM(n))



































