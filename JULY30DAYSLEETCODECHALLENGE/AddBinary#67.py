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

a = input()
b = input()
print(AddBinary(a, b))

























