#1394

def luckyInteger(arr):
    d = {}
    k = []
    for w in arr:
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1
    for keys in d:
        if d[keys] == keys:
            k.append(d[keys])
    if len(k) != 0:
        
        print(max(k))
    if len(k) == 0:
        print(-1)
arr = [int(x) for x in input().split()]
luckyInteger(arr)


from collections import Counter
def luckyInteger2(arr):
    s = -1
    a = Counter(arr)
    #print(a)
    b = list(set(arr))
    #print(b)
    for i in b:
        if i == a[i]:
            s = max(s, i)
    print(s)
    
arr = [int(x) for x in input().split()]
luckyInteger2(arr)









