#189

##def Rotate(arr, d):
##    for i in range(d):
##        
##        prev = arr[-1]
##        
##        for j in range(len(arr)):
##            
##            arr[j], prev = prev, arr[j]
##            
##    return arr
##
##n = int(input())
##arr = [int(x) for x in input().split()]
##d = int(input())
##print(Rotate(arr,d))


#using extra array
##def Rotate(arr, d):
##    n = len(arr)
##    a = [0] * n
##    for i in range(n):
##        a[(i + d) % n] = arr[i]
##    arr[:] = a
##    return arr
##
##n = int(input())
##arr = [int(x) for x in input().split()]
##d = int(input())
##print(Rotate(arr,d))

#3rd method
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
def Rotate(arr, d):
    n = len(arr)
    d %= n
    reverse(arr, 0, n - 1)
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    
    
n = int(input())
arr = [int(x) for x in input().split()]
d = int(input())
Rotate(arr,d)
print(arr)










