#160

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
    inputList=[int(ele)for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
def length(head):
    count = 0
    temp = head
    while(temp != None):
        count += 1
        temp = temp.next
    return count
def getIntersectionNode(headA, headB):
    lengthA = length(headA)
    lengthB = length(headB)
##    print(lengthA,"   ", lengthB)
    p = headA
    printLL(p)
    q = headB
    d = abs(lengthA - lengthB)
    #f = max(lengthA, lengthB)
    if lengthA > lengthB:
        
        while d:
            p = p.next
            d -= 1
    else:
        
        while d:
            q = q.next
            d -= 1
    while(p != q):
        p = p.next
        q = q.next
    return p
    #printLL(p.data)
        
            
    
        
   
headA = takeInput()
headB = takeInput()
skipA = int(input())
skipB = int(input())

##k = getIntersectionNode(headA, headB)
##printLL(k)
printLL(getIntersectionNode(headA, headB))
printLL(headA)













