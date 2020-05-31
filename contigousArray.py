#525

#length of subarray = currentIndex - mapindex
#if sum == 0 then currentIndex + 1


def contigousArrayLen(arr):
    mymap = {}
    summ = 0
    longest_subarray = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            summ = summ - 1
        else:
            summ += arr[i]
        
        if summ == 0:
            if(longest_subarray < i + 1):
                longest_subarray = i + 1
        
        elif summ in mymap:
            if longest_subarray < i - mymap[summ]:
                
                longest_subarray = i - mymap[summ]
        else:
            mymap[summ] = i
        print(mymap)
    return longest_subarray
            
        


arr = [int(x) for x in input().split()]
k = contigousArrayLen(arr)
print(k)
