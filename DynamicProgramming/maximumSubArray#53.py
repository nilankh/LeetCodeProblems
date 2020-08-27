#53
#page83
#kadane's algorithm
def maximumSubArray(arr):
    total_sum = max_sum = arr[0]
    for i in arr[1:]:
        total_sum = max(i, total_sum+ i)
        max_sum = max(max_sum, total_sum)
    return max_sum
        
    


arr = [int(x) for x in input().split()]
print(maximumSubArray(arr))


















