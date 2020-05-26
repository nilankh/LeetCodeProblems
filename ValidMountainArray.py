def validMountainArray(arr):
    increasing = True
    #Catch small and only decreasing Series
    if len(arr) < 3 or arr[0] >= arr[1]:
        return False
    for i in range(len(arr) - 1):
        #Decreasing Starts here and it was still increase till here
        #can be set only once
        #print("I value", i)
        if arr[i + 1] <= arr[i] and increasing :
            #print("increasing False hua for i",i)
            increasing = False
        if not increasing and arr[i + 1] >= arr[i]:
            #print("ye chala for what i",i)
            return False

    #catch only increasing array
    return True if not increasing else False
        


arr = [int(x) for x in input().split()]
if(validMountainArray(arr)):
    print("true")
else:
    print("false")
























