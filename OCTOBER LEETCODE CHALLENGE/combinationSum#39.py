#39
#103page

def combinationSum(candidates, target):
    if target == 0:
        return [[]]
    ans = []
    for i, n in enumerate(candidates):
        if target >= n:
            ans += [[n] + k for k in combinationSum(candidates[i:], target - n)]
    return ans

candidates = [int(x) for x in input().split()]
target = int(input())
print(combinationSum(candidates, target))


def comibationSumm(candidates, target):
    res = []
    if(len(candidates) == 0):
        return res;
    candidates.sort()

    toFindCombinationsToTarget(res, [], candidates, target, 0)
    return res

def toFindCombinationsToTarget(res, combination, candidates, target, startIndex):
    if target == 0:
        res.append(combination)
        return
    for i in range(startIndex, len(candidates)):
        if candidates[i] > target:
            continue
        
        combination.append(candidates[i])
        toFindCombinationsToTarget(res, combination, candidates, target - candidates[i], i)
        combination.pop()
        
candidates = [int(x) for x in input().split()]
target = int(input())
print(combinationSumm(candidates, target))    

    
















