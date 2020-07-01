#119
def getRow(n):
    row = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]
    return row

n = int(input())
print(getRow(n))
