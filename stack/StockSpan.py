def stockSpan(price,n):
    ans=[]
    ans.append(1)
    for i in range(1,n):
        c=1
        while i-c>=0 and price[i]>price[i-c]:
            c=c+ans[i-c]
        ans.append(c)
    return ans

n=int(input())
price=[int(ele) for ele in input().split()]
spans=stockSpan(price,n)
for ele in spans:
    print(ele,end=' ')
