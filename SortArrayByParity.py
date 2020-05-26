def sortArrayByParity(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            print(arr[i],end = ' ')
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            print(arr[i], end = ' ')

def sortArray(arr):
    arr.sort(key = lambda x: x % 2)
    return arr

arr = [int(x) for x in input().split()]
#sortArrayByParity(arr)
k = sortArray(arr)
print(k)
