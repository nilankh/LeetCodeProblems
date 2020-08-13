#1st way recursion 
##def knapsack(W, val, wt, n, i):
##
##    #base case
##    if i == n:
##        return 0
##
##    if wt[i] > W:
##        ans = knapsack(W, val, wt, n, i + 1)
##
##    else:
##        #inclusion of ith ite,
##        ans1 = val[i] + knapsack(W - wt[i], val, wt, n, i + 1)
##
##        #exclusion of the ith item
##        ans2 = knapsack(W, val, wt, n, i + 1)       
##        ans = max(ans1, ans2)
##    return ans
##
##
##val = [200, 300, 100]
##wt = [20, 25, 30]
##W = 50
##n = len(val)
##ans = knapsack(W, val, wt, n, 0)
##print(ans)



#2nd way
#overlapping problems in Knapsack
##recursion memoziation shared by student
##def knapsack(value,weight,w,i,n,dp):
##    if i==n:
##        return 0
##    
##    if weight[i]>w:
##        if dp[i+1][w]==-1:
##            ans=knapsack(value,weight,w,i+1,n,dp)
##            dp[i+1][w]=ans
##        else:
##            ans=dp[i+1][w]
##    else:
##        if dp[i+1][w-weight[i]]==-1:
##            small_ans1=knapsack(value,weight,w-weight[i],i+1,n,dp)
##            ans1=value[i]+small_ans1
##            dp[i+1][w-weight[i]]=small_ans1
##        else:
##            ans1=dp[i+1][w-weight[i]]+value[i]
##        if dp[i+1][w]==-1:
##            ans2=knapsack(value,weight,w,i+1,n,dp)
##            dp[i+1][w]=ans2
##        else:
##            ans2=dp[i+1][w]
##        ans=max(ans1,ans2)
##    return ans
##n=int(input())
##weight=[int(ele) for ele in input().split()]
##value=[int(ele1) for ele1 in input().split()]
##w=int(input())
##dp=[[-1 for j in range(w+1)]for i in range (n+1)]
##a=knapsack(value,weight,w,0,n,dp)
##print(a)

#3rd way iterative
def knapsack(W, val, wt):

    n = len(val)
    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]
    print(dp)
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            #print(j)

            if j < wt[i - 1]:
                ans = dp[i - 1][j]
            else:
                ans1 = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                ans2 = dp[i - 1][j]
                ans = max(ans1, ans2)
            dp[i][j] = ans
    return dp[n][W]
val = [20,30,40]
wt = [1,1,1]
W = 2
#val = [200, 300, 100]
#wt = [20, 25, 30]
#W = 50
n = len(val)
ans = knapsack(W, val, wt)
print(ans)































