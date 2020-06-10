def isSubsequence(s, t):

    for i in s:
        index = t.find(i)
        if index >= 0:
            t = t[index + 1:]
        else:
            return False
    return True
    
##    for i in s:
##        if i in t:
##            continue
##        else:
##            return False
##    return True


s = input()
t = input()
if(isSubsequence(s, t)):

    print("true")
else:
    print("false")
