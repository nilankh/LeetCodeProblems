#347
#rough pageno 59(pending)

def topKfreqElements(arr, k):
    arr.sort()
    d = {}
    
    for w in arr:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    print(d.sort())
    l = []
    for i in d:
        if d[i] >= k:
            l.append(i)
        if len(l) == 0:
            return l
    return l




arr = [int(x) for x in input().split()]
k = int(input())
f = topKfreqElements(arr, k)
print(f)















