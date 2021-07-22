#206


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
def reverse(head):
    curr=head
    prev=None
    while(curr is not None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head
head=takeInput()
l=reverse(head)
printLL(l)





