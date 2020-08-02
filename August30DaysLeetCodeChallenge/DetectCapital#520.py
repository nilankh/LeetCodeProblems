#520
#69page
def detectCapital(word):
    n = len(word)
    match1 = True
    match2 = True
    match3 = True

    #Case1: All Capital
    for i in range(n):
        if not word[i].isupper():
            match1 = False
            break
    if match1:
        return True

    #case2: ALL not Capital
    for i in range(n):
        if word[i].isupper():
            match2 = False
            break
    if match2:
        return True

    #case3 : All not Capital except First
    if not word[0].isupper():
        match3 = False
    if match3:
        for i in range(1, n):
            if word[i].isupper():
                match3 = False
    if match3:
        return True

    #if not matching
    return False
    
##word = input()
##print(detectCapital(word))

def detectCapital2(word):
    n = len(word)
    if len(word) == 1:
        return True

    #Case 1: ALL CAPITAL
    if word[0].isupper() and word[1].isupper():
        for i in range(2, n):
            if not word[i].isupper():
                return False

    #case 2 and case 3 (All not capital & all not capital except first)
    else:
        for i in range(1, n):
            if word[i].isupper():
                return False
    #if pass one of the cases
    return True
    

##word = input()
##print(detectCapital2(word))

def detectCapital3(word):
    return True if len(word) < 2 or word.isupper() or word[1:].islower() else False

word = input()
print(detectCapital3(word))









































