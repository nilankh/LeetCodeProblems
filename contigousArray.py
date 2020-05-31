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

#brute's force
def findLength(arr):
    maxLen = 0
    for start in range(len(arr)):
        zeroes = 0
        ones = 0
        for end in range(start, len(arr)):
            if arr[end] == 0:
                zeroes += 1
            else:
                ones += 1

            if(zeroes == ones):
                maxLen = max(maxLen, end - start + 1)
        return maxLen
        


arr = [int(x) for x in input().split()]
##k = contigousArrayLen(arr)
##print(k)
print(findLength(arr))






