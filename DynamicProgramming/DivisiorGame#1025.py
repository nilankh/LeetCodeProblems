#page no 73-75
def canWin(n):
    if n <= 1:
        return False
    for x in range(1,n):
        if(n % x == 0):
            if not canWin(n - x):
                return True
    return False

n = int(input())
print(canWin(n))



