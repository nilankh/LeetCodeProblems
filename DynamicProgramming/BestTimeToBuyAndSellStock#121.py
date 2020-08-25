#81
#121
import sys
##def maxProfit(price):
##    if not price:
##        return 0
##    ans = 0
##    mini = price[0]
##    for i in range(1, len(price)):
##        if price[i] < mini:
##            mini = price[i]
##        else:
##            ans = max(ans, price[i] - mini)
##    return ans
##
##price = [int(x) for x in input().split()]
##print(maxProfit(price))

def maxProfitR(price):
    if price == None or len(price) == 0:
        return 0
    return getMaxProfit(price, 0, sys.maxsize, 0)

def getMaxProfit(price, index, minStockPrice, maxDiff):
    if len(price) == index:
        return maxDiff
    earn = price[index] - minStockPrice
    maxDiff = max(earn, maxDiff)
    minStockPrice = min(minStockPrice, price[index])
    return getMaxProfit(price, index + 1, minStockPrice, maxDiff)


price = [int(x) for x in input().split()]
print(maxProfitR(price))














































