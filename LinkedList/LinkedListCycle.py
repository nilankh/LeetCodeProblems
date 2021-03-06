#141

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
    
##    for i in pos:
##        head = head.next
##    tail.next = 
    return head

#1st method
##def hasCycle(head):
##
##
##    d = {}
##    while(head):
##        if head in d:
##            return True
##        else:
##            d[head] = True
##        
##        head = head.next
##    
##    return False

#2nd method two pointer method
def hasCycle(head):
    if pos == -1:
        return False
    if head == None or head.next == None:
        return False
    slow = head
    fast = head.next
    while(slow != fast):
        if(fast == None and fast.next == None):
            return False
        slow = slow.next
        fast = fast.next.next
    return True


pos = int(input())

head = takeInput()

#printLL(head)

if(hasCycle(head)):
    print("true")
else:
    print("false")







