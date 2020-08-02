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
    




word = input()
print(detectCapital(word))











































