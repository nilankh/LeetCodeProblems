#392
#81 page
##def isSubsequence(s,t):
##    if len(s) == 0:
##        return True
##    if len(t) == 0:
##        return False
##    if(s[0] == t[0]):
##        return isSubsequence(s[1:],t[1:])
##
##    return isSubsequence(s,t[1:])

#two pointer method
'''
def isSubsequence(s,t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False
    s_idx = 0
##    t_idx = 0
    for i in range(len(t)):
        if(t[i] == s[s_idx]):
           s_idx += 1
        if(s_idx == len(s)):
           return True
    return s_idx == len(s)'''


s = input()
t = input()
print(isSubsequence(s,t))












