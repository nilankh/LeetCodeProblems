#118
def pascalTriangle(n):
    res = []
    for i in range(1, n + 1):
        l = []
        for j in range(1, i + 1):
            #begining and ending values
            if j == 1 or j == i:
                l.append(1)
            else:
                #and this is between values(u can refers amulya academy)
                l.append(res[-1][j - i - 1] + res[-1][j - i])
        res.append(l)
    return res


n = int(input())
k = pascalTriangle(n)
print(*k)
