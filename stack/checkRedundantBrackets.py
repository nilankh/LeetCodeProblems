def checkRedundant(string):
    count = 0
    s = []
    for i in string:
        if i != ')':
            s.append(i)

        if(i == ')'):
            while(s[-1] != '('):
                s.pop()
                count += 1
            s.pop()
            if count == 0:
                return True
        count = 0
    return False

string = input()
ans = checkRedundant(string)
if ans is True:
    print("true")
else:
    print("false")
