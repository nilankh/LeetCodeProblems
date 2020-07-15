#441
##FIRST METHOD
##def arrangeCoins(n):
##    if n < 2:
##        return n
##    else:
##        i = 1
##        count = 0
##        while count <= n:
##            count += i
##            i += 1
##        return i - 2

#2ND METHOD
def arrangeCoins(n):
    left = 0
    right = n
    while left <= right:
        k = (right + left)//2
        curr = k * (k + 1)//2
        if curr == n:
            return k
        if n < curr:
            right = k - 1
        else:
            left = k + 1
    return right


n = int(input())
print(arrangeCoins(n))
