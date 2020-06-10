#203

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
    return head
def removeLinkedList(head):
    curr = head
    prev = None

    
    while(curr != None):
        if head.next is None and val == head.data:
            return None
        if curr.data == val:
            if prev is None:
                head = head.next
                curr = head
            else:
                prev.next = curr.next
                curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return head


head = takeInput()
val = int(input())
printLL(removeLinkedList(head))











