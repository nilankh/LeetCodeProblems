#303
#89

#brute force method
##(Brute Force) [Time Limit Exceeded]
##Each time sumRange is called, we use a for loop to sum each individual element from index ii to jj.

##Complexity analysis:
##
##Time complexity : O(n)O(n) time per query. Each sumRange query takes O(n)O(n) time.
##
##Space complexity : O(1)O(1). Note that data is a reference to nums and is not a copy of it.


class NumArray:
    def __init__(self, arr):
        self.data = arr

    def sumRange(self, i, j):
        summ = 0
        k = i
        while(k <= j):
            summ += self.data[k]
            k += 1
        return summ

arr = [int(x) for x in input().split()]
obj = NumArray(arr)
param1 = obj.sumRange(0, 2)
print(param1)
param2 = obj.sumRange(2, 5)
print(param2)
param3 = obj.sumRange(0, 5)
print(param3)

















































