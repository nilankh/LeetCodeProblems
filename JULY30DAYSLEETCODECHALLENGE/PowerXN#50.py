#50
#rough page no 57

def power(x, n):
    f = (type(x) is float)
    if f: return float(x ** n)
    else: return x ** n

x = float(input())
n = int(input())
print(power(x, n))
