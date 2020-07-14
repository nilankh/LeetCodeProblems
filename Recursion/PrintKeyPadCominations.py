#PRINTKE CASE PEHLE HMKO APNA KAAM KRNA HOTA H FIR RECURSION SE
def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"
    return " "

def printKeypad(n,outputSoFar):
    if n == 0:
        print(outputSoFar)
        return
    smallNumber = n//10
    lastDigit = n % 10

    optionForLastDigit = getString(lastDigit)
    for c in optionForLastDigit:
        newOutput = c + outputSoFar
        printKeypad(smallNumber,newOutput)

#printKeypad(23,"")
n = int(input())
outputSoFar=""
printKeypad(n,outputSoFar)




