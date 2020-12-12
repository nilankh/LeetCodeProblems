#949
#90 page


def largestTimeForGivenDigits(arr):
    result = ""
    for i in range(4):
        for j in range(4):
            for k in range(4):
                #print("k", k)
                if i == j or j == k or k == i:
                    continue
                hh = str(arr[i]) + str(arr[j])
                mm = str(arr[k]) + str(arr[6 - i - j - k])
                timee = hh + ":" + mm
                #print("time", timee)
                if hh < "24" and mm < "60" and timee > result:
                    result = timee
    return result


arr = [int(d) for d in input().split()]
print(largestTimeForGivenDigits(arr))
