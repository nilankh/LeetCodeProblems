import sys
#1st way
def minStepsTo1(n):
    if n == 1:
        return 0
    ans1 = minStepsTo1(n - 1)
    ans2 = sys.maxsize
    if n % 2 == 0:
        ans2 = minStepsTo1(n//2)
    ans3 = sys.maxsize
    if n % 3 == 0:
        ans3 = minStepsTo1(n // 3)
    ans = min(ans1, min(ans2, ans3)) + 1;
    return ans




##n = int(input())
##ans = minStepsTo1(n)
##print(ans)




def minStepsTo1M(n, dp):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    if dp[n - 1] == -1:
        ans1 = minStepsTo1M(n - 1, dp)
        dp[n - 1] = ans1
    else:
        ans1 = dp[n - 1]

    
    ans2 = sys.maxsize
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minStepsTo1M(n//2)
            dp[n//2] = ans2
        else:
            ans2 = dp[n // 2]
            
    ans3 = sys.maxsize
    if n % 3 == 0:
        if dp[n // 3] == -1:
            ans3 = minStepsTo1M(n // 3)
            dp[n // 3] = ans3
        else:
            ans3 = dp[n //3]
            
    ans = min(ans1, min(ans2, ans3)) + 1;
    return ans




n = int(input())
dp = [-1 for i in range(n + 1)]
ans = minStepsTo1M(n, dp)
print(ans)



























































