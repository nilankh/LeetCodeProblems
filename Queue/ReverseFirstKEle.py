import queue

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
    q.put(ele)
k = int(input())
while(q.qsize() > 0):
    print(q.get())
    n -= 1
    
