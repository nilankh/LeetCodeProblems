import math
def PowerOfTwo(n):
    #k = 0
    #k = int(math.sqrt(n))
    if n < 1:
        return False
    while True:
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        n = n // 2
    
    

n = int(input())
if(PowerOfTwo(n)):
    print("true")
else:
    print("false")
