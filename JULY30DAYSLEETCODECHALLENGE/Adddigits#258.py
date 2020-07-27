#258
def AddDigits(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n = n // 10

        if n == 0 and summ > 9:
            n = summ
            summ = 0
    return summ
        

#Time O(1) Space O(1)
def Add(n):
    if(n == 0):
        return 0
    if n % 9 == 0:
        return 9
    else:
        return n % 9
    
n = int(input())
#print(AddDigits(n))
print(Add(n))
