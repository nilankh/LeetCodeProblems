#332
def coinChange(amount, coins):
    dp = [0 for i in range(amount + 1)]
    dp[0] = 1
    for c in coins:
        for j in range(c, amount + 1):
            dp[j] += dp[j - c]
        #print(dp)
    return dp[amount]




##amount = int(input())
##coins = [int(x) for x in input().split()]
##print(coinChange(amount, coins))

def coinChangeRR(amount, coins):
    return helper(amount, coins, 0)#0 index h

def helper(amount, coins, index):
    if amount == 0:
        return 1
    if amount < 0 or index == len(coins):
        return 0
    result = 0
    for i in range(index, len(coins)):
        if amount >= coins[i]:
            result += helper(amount - coins[i], coins, i)

    return result
amount = int(input())
coins = [int(x) for x in input().split()]
print(coinChangeRR(amount, coins))










