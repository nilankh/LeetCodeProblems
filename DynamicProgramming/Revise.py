def lis(arr, i, n):
    if i == n:
        return 0, 0

    im = 1
    for j in range(i + 1, n):
        if arr[j] >= arr[i]:
            fim = lis(arr, j, n)[0]
            im = max(im, 1 + fim)
    em = lis(arr, i + 1, n)[1]
    overall_max = max(im, em)
    return im, overall_max
def lisM(arr, i, n, dp):
    if i == n:
        return 0, 0
    im = 1
    for j in range(i + 1, n):
        if arr[j] >= arr[i]:
            if dp[j] == -1:
                ans = lisM(arr, j, n, dp)
                dp[j] = ans
                fm = ans[0]
            else:
                fm = dp[j][0]
            im = max(im, 1 + fm)
    if dp[i + 1] == -1:
        ans = lisM(arr, i + 1, n, dp)
        dp[i + 1] = ans
        em = ans[1]
    else:
        em = dp[i + 1][1]
    om = max(im, em)
    return im, om
        
n = int(input())
li = [int(p) for p in input().split()]
dp = [-1 for i in range(n + 1)]
ans = lisM(li, 0, n, dp)[1]
print(ans)



















