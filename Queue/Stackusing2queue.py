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
        while(self.q2.qsize()!=0):
            self.q1.put(self.q2.get())
        return ans
        #dono method sahi h   
            
    def top(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        ans = self.q1.get()
        self.q2.put(ans)
        self.q1,self.q2 = self.q2,self.q1 
        #self.count-=1
        return ans
        
    def getSize(self):
        return self.q1.qsize()





    
