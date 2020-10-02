#933
#103 Page
from collections import deque
class RecentCounter:
    def __init__(self):
        self.q = deque()
        



    def ping(self, t):
        self.q.append(t)
##  delete from the front all the pings which occured before 3000sec from now
        while(self.q) and (self.q[0] < (t - 3000)):
            self.q.popleft()
        return len(self.q)
        

obj = RecentCounter()
param1 = obj.ping(1)
print(param1)
param2 = obj.ping(100)
print(param2)
param3 = obj.ping(3001)
print(param3)
param4 = obj.ping(3002)
print(param4)

















