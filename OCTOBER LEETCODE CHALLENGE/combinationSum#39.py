#39
#103page

##def combinationSum(candidates, target):
##    if target == 0:
##        return [[]]
##    ans = []
##    for i, n in enumerate(candidates):
##        if target >= n:
##            ans += [[n] + k for k in combinationSum(candidates[i:], target - n)]
##    return ans
##
##candidates = [int(x) for x in input().split()]
##target = int(input())
##print(combinationSum(candidates, target))


def combinationSumm(candidates, target):
    res = []
    if(len(candidates) == 0):
        return res;
    dfs(candidates, target,[], res)
    return res

def dfs(candidates, target, path, res):
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return
    for i in range(len(candidates)):
        if candidates[i] > target:
            continue
        
        dfs(candidates[i:], target - candidates[i], path + [candidates[i]], res)
        
candidates = [int(x) for x in input().split()]
target = int(input())
print(combinationSumm(candidates, target))     

    
















