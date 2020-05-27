#961
def RepeatedElements(arr):
    for i in range(len(arr)):
        
        for j in range(len(arr)):
            
            if(arr[i] == arr[j] and i != j):
                return arr[i]
    #return arr[i]
            

def RepeatByDict(arr):
    d = {}
    for w in arr:
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1
    
    for keys in d:
        if d[keys] > 1:
            return keys
        
    #print(d)

arr = [int(x) for x in input().split()]
#k = RepeatedElements(arr)
k = RepeatByDict(arr)
print(k)




    
