#167
def twoSum(arr, target):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == target:
            return [i + 1, j + 1]
        elif arr[i] + arr[j] > target:
            j = j -1
        else:
            i += 1
    return [-1, -1]
    

arr = [int(x) for x in input().split()]
target = int(input())
k = twoSum(arr, target)
print(k)
