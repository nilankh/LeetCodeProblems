#70
def climbingStairs(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbingStairs(n - 2) + climbingStairs(n - 1)
    


n = int(input())
print(climbingStairs(n))





