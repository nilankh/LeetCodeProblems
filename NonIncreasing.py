def NonDecreasingArray(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            count += 1
            if count >= 2:
                return False
            elif (i - 1) >= 0 and arr[i + 1] < arr[i - 1]:
                arr[i + 1] = arr[i]
    return True

    

arr = [int(x) for x in input().split()]
k = NonDecreasingArray(arr)
print(k)
