#392
#81 page
def isSubsequence(s,t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False
    if(s[0] == t[0]):
        return isSubsequence(s[1:],t[1:])

    return isSubsequence(s,t[1:])



s = input()
t = input()
print(isSubsequence(s,t))












