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
        
    
    

    


n = int(input())
print(AddDigits(n))
