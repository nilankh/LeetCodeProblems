import queue
class StackUsingQueues:
    
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        #self.count=0
        
        
    def push(self,data):
        self.q1.put(data)
        
       

    
    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        ans = self.q1.get()
