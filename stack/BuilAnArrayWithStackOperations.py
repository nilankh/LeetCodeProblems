#1441
def BuildAnArrayWithStackOperations(target):
    ans = []
    i = 0
    num = 1
    while i < len(target):
        while target[i] != num:
            ans.append("Push")
            ans.append("Pop")
            num += 1
        ans.append("Push")
        num += 1
        i +=1
    return ans




target = [int(c) for c in input().split()]
n = int(input())
k = BuildAnArrayWithStackOperations(target)
print(*k)
