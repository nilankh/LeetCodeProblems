#PRINTKE CASE PEHLE HMKO APNA KAAM KRNA HOTA H FIR RECURSION SE
def printMin(l, minSoFar = 100000000):
    if len(l) == 0:
        print(minSoFar)
        return
    newMin = min(minSoFar, l[0])
    printMin(l[1:], newMin)
printMin([1,2,3,4,5,-1,0,-2,-4,-5,6])
