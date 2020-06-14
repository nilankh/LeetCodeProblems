def isBalanced(string):
    s = []
    for char in string:
        print("char", char)
        if char in '({[':
            s.append(char)
            print(s)
        elif char is ')':
            if not s or s[-1] != '(':
                return False
            s.pop()
        elif char is '}':
            if not s or s[-1] != '{':
                return False
            s.pop()

        elif char is ']':
            if not s or s[-1] != '[':
                return False
            s.pop
    if not s:
        return True
    return False
            

string = input()
ans = isBalanced(string)
print(ans)
