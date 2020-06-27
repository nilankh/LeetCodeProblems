#1450
def busyStudents(startTime, endTime, queryTime):
    count = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime and endTime[i] >= queryTime:
            count += 1
    return count



startTime = [int(c) for c in input().split()]
endTime = [int(fu) for fu in input().split()]
queryTime = int(input())
print(busyStudents(startTime, endTime, queryTime))
