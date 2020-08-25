#81
#121



def maxProfit(price):
    if not price:
        return 0
    ans = 0
    mini = price[0]
    for i in range(1, len(price)):
        if price[i] < mini:
            mini = price[i]
        else:
            ans = max(ans, price[i] - mini)
    return ans

price = [int(x) for x in input().split()]
print(maxProfit(price))























