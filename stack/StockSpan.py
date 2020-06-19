def stockSpan(price,n):
    ans=[]
    ans.append(1)
    for i in range(1,n):
        c=1
        while i-c>=0 and price[i]>price[i-c]:
            c=c+ans[i-c]
        ans.append(c)
    return ans
def stockSpan2(price, n):
    s = []
    output = []
    s.append(0)
    output.append(1)

    for i in range(1, len(price)):
        while(len(s) != 0 and price[s[-1]] < price[i]):
            s.pop()
        if len(s) == 0:
            output.append(i + 1)
        else:
            output.append(i - s[-1])
        s.append(i)
    return output
n=int(input())
price=[int(ele) for ele in input().split()]
spans=stockSpan2(price,n)
for ele in spans:
    print(ele,end=' ')
