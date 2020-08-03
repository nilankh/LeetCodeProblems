#705
#page 71

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numBuckets = 15000
        self.buckets = [[] for i in range(self.numBuckets)]

    def hash_function(self, key):
        return key % self.numBuckets

    def add(self, key):
        i = self.hash_function(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self, key):
        i = self.hash_function(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, key):
        """
        returns True if this set contains the specified element
        """
        i = self.hash_function(key)
        if key in self.buckets[i]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.remove(1)
param_3 = obj.contains(1)
print(param_3)

















        
