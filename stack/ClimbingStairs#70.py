#70
'''
def climbingStairs(n):
    #this will give tle
    if n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 3
    else:return climbingStairs(n - 2) + climbingStairs(n - 1)

##from sys import setrecursionlimit
##setrecursionlimit(100000)
n = int(input())
print(climbingStairs(n))
'''

def climbingStairs(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
    return b


n = int(input())
print(climbingStairs(n))










