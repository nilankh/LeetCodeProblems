#142

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")
    return
def takeInput():
    inputList=[int(ele) for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next=newNode
            tail=newNode
    #printLL(tail)

    if pos == -1:
        return False
    curr = head
    for i in range(1, pos):
        curr = curr.next
    tail.next = curr
    return head

def hasCycle(head):
    
##    1st method
##    d ={}
##    curr = head
##    while(curr):
##        print(str(curr))
##        if curr in d.keys():
##            return curr
##        else:
##            d[curr] = 1
##            curr = curr.next
##    return None

    #2nd method
    seen = {None}
    while head not in seen:
        seen.add(head)
        head = head.next
    return head



    
pos = int(input())
head = takeInput()
#printLL(head)
printLL(hasCycle(head))
#printLL(k)











    
