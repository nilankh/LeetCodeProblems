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












































