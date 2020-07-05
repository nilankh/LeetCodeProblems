#normal
'''
def fact(n):
    if n == 0:
        return 1
    smallOutput = fact(n-1)
    return n * smallOutput
print(fact(5))'''

#Another Method
'''
def fact(n):
    if n == 0:
        return 1
    smallOutput = fact(n-1)
    output = n * smallOutput
    print(output)
    return output

fact(5)'''

#Hack method
'''
def factHelper(n):
    if n == 0:
        return 1

    smallOutput = factHelper(n-1)
    output = n * smallOutput
    return output

def fact(n):
    output = factHelper(n)
    print(output)
fact(5)'''
#without returning just prinitng

def printFact(n,ans):
    if n == 0:
        print(ans)
        return
    ans = ans * n
    printFact(n-1,ans)

printFact(5,1)














    
