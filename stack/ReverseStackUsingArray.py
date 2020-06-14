def reverseStackUsingArray(s1, s2):
    if len(s1) <= 1:
        return
    while len(s1) != 1:
        ele = s1.pop()
        s2.append(ele)
    last_element = s1.pop()
    while len(s2) != 0:
        ele = s2.pop()
        s1.append(ele)
    reverseStackUsingArray(s1, s2)
    s1.append(last_element)
    
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStackUsingArray(s1, s2)
while(len(s1) != 0):
    print(s1.pop(), end = " ")
