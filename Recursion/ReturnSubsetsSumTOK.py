def subsets(arr, k):
    return subsetsHelper(arr, 0, k)

def subsetsHelper(arr, si, k):
    if si == len(arr):
        if k == 0:
            return [list()]
        else:
            return list()

    smallOutput1 = subsetsHelper(arr, si + 1, k)
    smallOutput2 = subsetsHelper(arr, si + 1, k - arr[si])

    output = (len(smallOutput1) + len(smallOutput2)) * [0]
    index = 0
    for i in range(len(smallOutput1)):
        output[index] = smallOutput1[i]
        index += 1

    for i in range(len(smallOutput2)):
        output[index] = (len(smallOutput2[i]) + 1) * [0]
        output[index][0] = arr[si]

        for j in range(len(smallOutput2[i])):
            output[index][j + 1] = smallOutput2[i][j]
        index += 1
    return output
    

n = int(input())
arr = [int(x) for x in input().split()]
k = int(input())
output = subsets(arr, k)
print(*output)
