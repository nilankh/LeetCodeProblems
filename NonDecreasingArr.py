#665

def NonDecreasingArray(arr):
    count = 0
    for i in range(len(arr) - 1):
        
        if arr[i] > arr[i + 1]:
            count += 1
            
            if count >= 2:
                return False
                
            elif (i - 1) >= 0 and arr[i + 1] < arr[i - 1]:
                
                #print("cha;a")
                arr[i + 1] = arr[i]
                #print(arr)
              
    return True
    
    

arr = [int(x) for x in input().split()]
k = NonDecreasingArray(arr)
if(k):
    print("true")
else:
    print("false")

#ex=3 4 2 3, ex 3 4 2
