#746
#page no 79
def minimumCostClimbingStaris(cost):
    return min(helper(cost, 0), helper(cost, 1))
def helper(cost, x):
    if x >= len(cost):
        return 0
    k = min(helper(cost, x + 1), helper(cost, x + 2)) + cost[x]
    return k
cost = [int(x) for x in input().split()]
print(minimumCostClimbingStaris(cost))


#memoization
##def minimumCostClimbingStarisRM(cost):
##    dp = [None for i in range(len(cost) + 1)]
##    return min(helper2(cost, 0, dp), helper2(cost, 1, dp))
##def helper2(cost, index, dp):
##    if index >= len(cost):
##        return 0
##    if dp[index] == None:
##        dp[index] = min(helper2(cost, index + 1, dp), helper2(cost, index + 2, dp)) + cost[index]
##        
##    return dp[index]
##
##cost = [int(x) for x in input().split()]
##print(minimumCostClimbingStarisRM(cost))










































