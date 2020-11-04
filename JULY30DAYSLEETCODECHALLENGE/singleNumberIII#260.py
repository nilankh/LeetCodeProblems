#260
def singleNumber(arr):
    d = {}
    for w in arr:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    k = []
    for i in d:
        if d[i] == 1:
            k.append(i)
    return k
arr = [int(x) for x in input().split()]
k = singleNumber(arr)
print(*k)




