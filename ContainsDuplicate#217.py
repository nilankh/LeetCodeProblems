#217
def containsDuplicate(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for i in d:
        if d[i] > 1:
            return True
    return False
arr = [int(x) for x in input().split()]
print(containsDuplicate(arr))












