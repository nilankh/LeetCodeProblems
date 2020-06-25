import queue


def reverseFirstK(q, k):
    reverseQueue(q, k)
    n = q.qsize()
    for i in range(n - k):
        q.put(q.get())
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
    q.put(ele)
k = int(input())
reverseFirstK(q, k)
while(q.qsize() > 0):
    print(q.get())
    n -= 1
    
