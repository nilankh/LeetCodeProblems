def LIS(li, i, n):

    if i == n:
        return 0, 0
    
    including_max = 1#including myself
    for j in range(i + 1, n):
        
        #print(j)
        if li[j] >= li[i]:
            further_including_max = LIS(li, j, n)[0]
            #print(further_including_max)
            including_max = max(including_max, 1 + further_including_max)
            #print(including_max)
    excluding_max = LIS(li, i + 1, n)[1]
    #print(excluding_max)
    overallMax = max(including_max, excluding_max)
    #print(overallMax)
    return including_max, overallMax

        
n = int(input())
li = [int(ele) for ele in input().split()]
ans = LIS(li, 0, n)[1]
print(ans)
