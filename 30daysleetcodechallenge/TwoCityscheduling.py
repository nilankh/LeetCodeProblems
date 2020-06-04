#1029
'''
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000'''

##def twoCity(cost):
##
##    refund = []
##    n = len(cost) // 2
##    minCost = 0
##    for a, b in cost:
##        #print("a", a , "    ", "b", b)
##        refund.append(b - a)
##        minCost += a
##        #print("mincos", minCost)
##    refund.sort()
##    #print('refund',refund)
##    for i in range(n):
##        minCost += refund[i]
##    return minCost

def twoCity(costs):
    costs = sorted(costs, key = lambda x:x[0]-x[1])
    #print(costs)
    n = len(costs)
    cost = 0
    for c in costs[:int(n/2)]:
        #print("c",c)
        cost += c[0]
        #print("costgs",cost)
    for c in costs[int(n/2):]:
        #print("****************")
        #print("c",c)
        cost += c[1]
        #print("costsssd",cost)
    return cost



str = input().split()
n, m = int(str[0]), int(str[1])
b = str[2:]
costs= [[int(b[m * i + j]) for j in range(m)] for i in range(n)]

print(twoCity(costs))














