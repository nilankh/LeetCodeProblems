#1385

def findTheDistance(arr1, arr2):
    res = len(arr1)
    for i in range(len(arr1)):
        #print("i chala", i)
        for j in range(len(arr2)):
            #print("j chala", j)
            if(abs(arr1[i] - arr2[j])) > d:
                
                continue
            else:
                res -= 1
                break
                
    return res
                
    

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
d = int(input())
print(findTheDistance(arr1, arr2))
