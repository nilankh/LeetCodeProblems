##import sys
##def MCM(p, i, j):
##
##    if i == j:
##        return 0
##    
##    min_value = sys.maxsize
##    for k in range(i, j):
##        ans1 = MCM(p, i, k)
##        ans2 = MCM(p, k + 1, j)
##
##        mCost = p[i - 1] * p[k] * p[j]
##        curr_value = ans1 + ans2 + mCost
##        min_value = min(min_value, curr_value)
##
##    return min_value
##        
##
##p = [2,3,4,5,6]#it means we have 4matrices A->2 X 3; B-> 3 X 4; C ->4 X 5; D-> 5 X 6
##n = len(p) - 1 #it represents the number of matrices
##
##ans = MCM(p, 1, n)
##print(ans)


#2nd approach

import sys
def MCM(p, i, j, dp):

    if i == j:
        return 0
    
    min_value = sys.maxsize
    for k in range(i, j):
        if dp[i][k] == -1:
            
            ans1 = MCM(p, i, k, dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]

        if dp[k + 1][j] == -1:
            
            ans2 = MCM(p, k + 1, j, dp)
            dp[k + 1][j] = ans2
        else:
            ans2 = dp[k + 1][j]
            
        mCost = p[i - 1] * p[k] * p[j]
        curr_value = ans1 + ans2 + mCost
        min_value = min(min_value, curr_value)

    return min_value
        

p = [2,3,4,5,6]#it means we have 4matrices A->2 X 3; B-> 3 X 4; C ->4 X 5; D-> 5 X 6
n = len(p) - 1 #it represents the number of matrices
dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]
ans = MCM(p, 1, n, dp)
print(ans)
