#1122

def RelativeSort(arr1, arr2):
    d1 = {}
    k1 = []
    k2 = []
##    d2 = {}
    for w in arr1:
        if w in d1:
            d1[w] += 1
        else:
            d1[w] = 1
    #print("ye d1 h", d1)
##    for k in arr2:
##        if k in d2:
##            d2[k] += 1
##        else:
##            d2[k] = 1
    #print("ye d2 h ", d2)
    for i in arr2:
        while d1[i]:
            k1.append(i)
            d1[i] -= 1
        del d1[i]
        #print("deleted d1", d1)
    #print("bacha d1", d1)
    for i in d1.keys():
        while d1[i]:
            k2.append(i)
            d1[i] -=1
        #print("list2",list2)
    print(k1 + k2)
            


arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
RelativeSort(arr1, arr2)
