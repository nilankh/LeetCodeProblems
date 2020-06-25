#287
def findD(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
        
def findD2(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return arr[i]
arr = [int(x) for x in input().split()]
print(findD2(arr))
