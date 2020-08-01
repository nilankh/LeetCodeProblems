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

n = int(input())
li = [int(p) for p in input().split()]
ans = lis(li, 0, n)[1]
print(ans)
