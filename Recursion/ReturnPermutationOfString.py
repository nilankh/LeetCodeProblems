def permutation(string):
    if len(string) == 1:
        return [string]
    result = []
    for i, v in enumerate(string):
        result += [v + p for p in permutation(string[:i] + string[i + 1:])]
    return result
        

string = input()
ans = permutation(string)
for ele in ans:
    print(ele)


##string = "abc"
##for i, v in enumerate(string):
##    print(i, v)
    
##output of this
## 0 a
##1 b
##2 c
