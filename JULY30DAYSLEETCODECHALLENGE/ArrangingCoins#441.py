#441

def arrangeCoins(n):
    if n < 2:
        return n
    else:
        i = 1
        count = 0
        while count <= n:
            count += i
            i += 1
        return i - 2

n = int(input())
print(arrangeCoins(n))
