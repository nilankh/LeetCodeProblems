#344
def reverseString(s, start, end):
    if len(s) == 0:
        return
    if len(s) == 1:
        return s
    if start < end:
        s[start], s[end] = s[end], s[start]
        reverseString(s, start + 1, end - 1)
    return s

#s = ["h","e","l","l","o"]
s = [str(x) for x in input().split()]
print(reverseString(s, 0, len(s) - 1))
