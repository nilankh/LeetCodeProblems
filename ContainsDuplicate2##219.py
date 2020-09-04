#219
#95page
##TLE APPROACH
def containsDuplicate(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                t = abs(i - j)
                if t <= k:
                    return True
    return False

arr = [int(k) for k in input().split()]
k = int(input())
print(containsDuplicate(arr, k))

















