#332
def coinChange(amount, coins):
    dp = [0 for i in range(amount + 1)]
    dp[0] = 1
    for c in coins:
        for j in range(c, amount + 1):
            dp[j] += dp[j - c]
    return dp[amount]




amount = int(input())
coins = [int(x) for x in input().split()]
print(coinChange(amount, coins))
