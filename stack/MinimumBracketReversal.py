def countBracketReversals(string):

    if len(string) == 0:
        return 0
    if len(string) % 2 != 0:
        return -1
    




string = input()
ans = countBracketReversals(string)
print(ans)
