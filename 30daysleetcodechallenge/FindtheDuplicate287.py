#287
def findD(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
        
    
arr = [int(x) for x in input().split()]
print(findD(arr))
