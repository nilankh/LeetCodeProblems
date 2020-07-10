def SubsetArray(arr):
    

n = int(input())
arr = [int(c) for c in input().split()]
output = SubsetArray(arr)
for lst in output:
    for num in lst:
        print(num, end = ' ')
    print()
