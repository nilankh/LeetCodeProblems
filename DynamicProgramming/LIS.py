#checkout the rough 33 35
##def LIS(li, i, n):
##
##    if i == n:
##        return 0, 0
##    
##    including_max = 1#including myself
##    for j in range(i + 1, n):
##        
##        #print(j)
##        if li[j] >= li[i]:
##            further_including_max = LIS(li, j, n)[0]
##            #print(further_including_max)
##            including_max = max(including_max, 1 + further_including_max)
##            #print(including_max)
##    excluding_max = LIS(li, i + 1, n)[1]
##    #print(excluding_max)
##    overallMax = max(including_max, excluding_max)
##    #print(overallMax)
##    return including_max, overallMax
##
##        
##n = int(input())
##li = [int(ele) for ele in input().split()]
##ans = LIS(li, 0, n)[1]
##print(ans)




 





#MEmoization
##def LIS(li, i, n, dp):
##
##    if i == n:
##        return 0, 0
##    
##    including_max = 1#including myself
##    for j in range(i + 1, n):
##        
##        if li[j] >= li[i]:
##            if dp[j] == -1:
##                ans = LIS(li, j, n, dp)
##                dp[j] = ans
##                further_including_max = ans[0]
##            else:
##                further_including_max = dp[j][0]
##            including_max = max(including_max, 1 + further_including_max)
##
##    if dp[i + 1] == -1:
##        ans = LIS(li, i + 1, n, dp)
##        dp[i + 1] = ans
##        excluding_max = ans[1]
##    else:
##        excluding_max = dp[i + 1][1]
##        
##    overallMax = max(including_max, excluding_max)
##    return including_max, overallMax
##
##        
##n = int(input())
##li = [int(ele) for ele in input().split()]
##dp = [-1 for i in range(n + 1)]
##ans = LIS(li, 0, n, dp)[1]
##print(ans)





#3rd way iterative time complexity(n^2) 

def LISI(li, n):

    dp = [[0 for j in range(2)] for i in range(n + 1)]
    #print(dp)

    for i in range(n - 1, -1, -1):
        #print(i)
        including_max = 1
        for j in range(i + 1, n):
            #print(j)
            if li[j] > li[i]:
                including_max = max(including_max, 1 + dp[j][0])
                #print(including_max)
        dp[i][0] = including_max
        #print(dp[i][0])
        excluding_max = dp[i + 1][1]
        #print(excluding_max)
        overallMax = max(including_max, excluding_max)
        #print(overallMax)
        dp[i][1] = overallMax
        #print(dp[i][1])
        
    return dp[0][1]

n = int(input())
li = [int(ele) for ele in input().split()]
ans = LISI(li, n)
print(ans)



















































