#1290


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()
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

def convertBinaryToInt(head):

    result = 0
    while head:
        result = result * 2 + head.data
        head = head.next
    return result
    


head = takeInput()
k = convertBinaryToInt(head)
print(k)









