#528
'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.'''


import random
class Solution:
        def __init__(self, w):
            self.prefix_sum = []
            prefix_sum = 0
            for weight in w:
                prefix_sum += weight
                self.prefix_sum.append(prefix_sum)
            self.total_sum = prefix_sum
    
        def pickIndex(self)-> int:
            
            random_num = self.total_sum * random.random()
            low, high = 0, len(self.prefix_sum)
            while low < high:
                mid = low + (high - low) // 2
                if random_num > self.prefix_sum[mid]:
                    low = mid + 1
                else:
                    high = mid
            return low



w = [1, 3]
k = pickIndex(w)
print(k)



    

