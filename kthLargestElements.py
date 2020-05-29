#215

#we can solve this by using priority queue too

def KthLargest(arr):
    return sorted(arr)[-k]

arr = [int(x) for x in input().split()]
k = int(input())
j = KthLargest(arr)
print(j)
