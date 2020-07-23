def validatePan(string):
    if len(string) > 10 :
        return False
    if len(string) < 10:
        return False
    vari = []
    starting = 'A'
    for i in range(0, 26):
        vari.append(starting)
        starting = chr(ord(starting) + 1)
##    print(vari)
    k = string[-1]
    for i in k:
        if i in vari:
            continue
        else:
            return False
        
    m = string[:5]
    for i in m:
        if i in vari:
            continue
        else:
            return False
    return True

    number = string[5:9]
    new = []
    n1 = 0
    for i in range(0, 10):
        new.append(n1)
        n1 += 1
    for i in number:
##        print(i, " ", type(i))
        if i in new:
            continue
        else:
            return False
    return True
        
string = input()

k = validatePan(string)
print(k)

def validatePAN(pan):
	pan = str(pan)  #ABCDE1234F
	if (len(pan) == 10) and (pan[0:5].isalpha()) and (pan[5:9].isdigit()) and (pan[-1].isalpha()):
		return True
	return False












