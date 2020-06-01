#526


#BRUTEFORCE

##count = 0
##def countArrangement(n):
##
##    global count
##    
##    arr = [0] * n
##    for i in range(1, n + 1):
##        arr[i - 1] = i
##    
##    permute(arr, 0)
##    
##    return count
##        
##    
##def permute(arr, l):
##    global count
##    if(l == len(arr) - 1):
##        i = 1
##        while(i <= len(arr)):
##            if arr[i - 1] % i != 0 and i % arr[i - 1] != 0:
##                break
##            i+= 1        
##        if(i == len(arr) + 1):
##            count += 1
##            
##    for i in range(l, len(arr)):
##        
##        swap(arr, i, l)
##        permute(arr, l + 1)
##        swap(arr, i, l)
##
##def swap(arr, x, y):
##    temp = arr[x]
##    arr[x] = arr[y]
##    arr[y] = temp
##    

##from sys import setrecursionlimit
##setrecursionlimit(10000)
##n = int(input())
##
##k = countArrangement(n)
##print(k)



#BRUTE FORCE ACCEPTED

##count = 0
##def countArrangementA(n):
##
##    global count
##    
##    arr = [0] * n
##    for i in range(1, n + 1):
##        arr[i - 1] = i
##    
##    permuteA(arr, 0)
##    
##    return count
##        
##    
##def permuteA(arr, l):
##    global count
##    if(l == len(arr)):
##        count += 1
##    for i in range(l, len(arr)):
##        
##        swapA(arr, i, l)
##        if(arr[l] %(l + 1) == 0 or (l + 1) % arr[l] == 0):
##            permuteA(arr, l + 1)
##        swapA(arr, i, l)
##  
##
##def swapA(arr, x, y):
##    temp = arr[x]
##    arr[x] = arr[y]
##    arr[y] = temp
##    
##
##from sys import setrecursionlimit
##setrecursionlimit(10000)
##n = int(input())
##
##k = countArrangementA(n)
##print(k)

#BackTracKing

count = 0
def countArrangement(n):
    global count
    visited = [False for i in range(n + 1)]
    calculate(n, 1, visited)
    return count

def calculate(n, pos, visited):
    global count
    if(pos > n):
        count += 1
        return
    for i in range(1, n + 1):
        if(visited[i] is False and (pos % i == 0 or i % pos == 0)):
            visited[i] = True
            calculate(n, pos + 1, visited)
            visited[i] = False
            
n = int(input())
k = countArrangement(n)
print(k)





























