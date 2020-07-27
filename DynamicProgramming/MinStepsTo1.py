import sys
def minStepsTo1(n):
    if n == 1:
        return 0
    ans1 = minStepsTo1(n - 1)
    ans2 = sys.maxsize
    if n % 2 == 0:
        ans2 = minStepsTo1(n//2)
    ans3 = sys.maxsize
    if n % 3 == 0:
        ans3 = minStepsTo1(n // 3)
    ans = min(ans1, min(ans2, ans3)) + 1;
    return ans




n = int(input())
ans = minStepsTo1(n)
print(ans)











































