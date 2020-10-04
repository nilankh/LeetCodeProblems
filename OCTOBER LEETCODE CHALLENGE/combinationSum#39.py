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


   

    
















