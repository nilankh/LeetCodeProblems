def FindStep(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return FindStep(n-3)+FindStep(n-2)+FindStep(n-1)
n=int(input())
print(FindStep(n))
