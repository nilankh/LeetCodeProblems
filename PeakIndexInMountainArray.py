#852


##def PeakMountain(arr):
##    for i in range(len(arr)):
##        if(arr[i] < arr[i + 1]):
##            continue
##        return i


def PeakMountain(arr):
    for i in range(len(arr)):
        if(arr[i] > arr[i + 1]):
            return i

def PeakMountainB(arr):
    low = 0
    high = len(arr) - 1
    while(low < high):
        mid = (low + high)//2
        if(arr[mid] < arr[mid + 1]):
            low = mid + 1
        else:
            high = mid
    return low
            
        


n = int(input())
arr = [int(x) for x in input().split()]
k = PeakMountain(arr)

print(k)
