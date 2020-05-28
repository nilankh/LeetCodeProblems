#81
def searchInRotate(arr):
    #return target in arr
    if target in arr:
        return True
    return False

    
#sahi h
##    for i in arr:
##        if i == target:
##            return True
##    else:
##        return False


arr = [int(x) for x in input().split()]
target = int(input())
if(searchInRotate(arr)):
    print("true")
else:
    print("false")
