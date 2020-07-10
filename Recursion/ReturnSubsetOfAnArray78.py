def SubsetArray(arr):
    n = len(arr)
    if n <= 0:
        output = [list()]
        return output
    smallerOutput = SubsetArray(arr[1:])
    return smallerOutput + [[arr[0]] + b for b in smallerOutput]

    

n = int(input())
arr = [int(c) for c in input().split()]
output = SubsetArray(arr)
for lst in output:
    for num in lst:
        print(num, end = ' ')
    print()













