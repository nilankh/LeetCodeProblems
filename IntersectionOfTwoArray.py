#349


def intersection(arr1, arr2):
    c= set(arr1)
    d = set(arr2)
    k = c.intersection(d)
    print(list(k))



arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
intersection(arr1, arr2)
