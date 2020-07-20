#67
def AddBinary(a, b):
    
    result = ""
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    while(i >= 0 or j >= 0):
        summ = carry
        if i >= 0:
            summ += ord(a[i]) - ord('0')
        i-= 1
        if j >= 0:
            summ += ord(b[j]) - ord('0')
        j -= 1
        carry = 1 if summ > 1 else 0
        result += str(summ % 2)
    if carry != 0 : result += str(carry)
    return result[::-1]



def AddBinary2(a, b):
    carry = 0
    result = ""
    i = 0
    alen = len(a)
    blen = len(b)
    while(i < alen or i < blen or carry != 0):
        x = 0
        if i < alen and a[alen - 1 - i] == '1':
            x = 1
        y = 0
        if i < blen and b[blen - 1 - i] == '1':
            y = 1
        result = (x + y + carry)%2 + result
        carry = (x + y + carry)//2
        i+= 1
    return result
    

a = input()
b = input()
print(AddBinary2(a, b))























