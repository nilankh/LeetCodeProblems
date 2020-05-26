def sortArrayByParity(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            print(arr[i],end = ' ')
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            print(arr[i], end = ' ')


arr = [int(x) for x in input().split()]
sortArrayByParity(arr)
