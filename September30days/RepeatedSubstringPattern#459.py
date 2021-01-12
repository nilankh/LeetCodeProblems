#459
#page99
##def repeatedSubstringPatter(string):
##    
##
##
##string = input()
##print(repeatedSubstringPatter(string))


string = "abab"
d = {}
for w in string:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1
print(d)







































