#198

#wrong approach 
##import sys
##def houseRobber(arr):
##    maxAdd = -999999999999
##    i = 0
##    j = 1
##    summ = 0
##    summ2 = 0
##    while(i < len(arr)):
##        summ = summ + arr[i]
##        i += 2
##    print(summ)
##    while j < len(arr):
##        summ2 = summ2 + arr[j]
##        j += 2
##    return max(summ, summ2)

#correct by recursion
##def houseRobber(arr):
##    return helper(arr, 0)
##def helper(arr, currentIndex):
##    if currentIndex >= len(arr):
##        return 0
##    stealCurrent = arr[currentIndex] + helper(arr, currentIndex + 2)
##    skipCurrent = helper(arr, currentIndex + 1)
##
##    return max(stealCurrent, skipCurrent)
    

def houseRobberMemo(arr):
    dp = [0 for i in range(len(arr) + 1)]
    return houseRobberMemoHelper(arr, 0, dp)
def houseRobberMemoHelper(arr, currentIndex, dp):
    if currentIndex >= len(arr):
        return 0
    if dp[currentIndex] != 0:
        return dp[currentIndex]
    
    stealCurrent = arr[currentIndex] + houseRobberMemoHelper(arr, currentIndex + 2, dp)
    skipCurrent = houseRobberMemoHelper(arr, currentIndex + 1, dp)
    return dp[currentIndex] + max(stealCurrent, skipCurrent)
    
arr = [int(l) for l in input().split()]
print(houseRobberMemo(arr))



















