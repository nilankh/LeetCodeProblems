#61

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end = "")
        head = head.next
    print()
    return

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count

def RotateLL(head, k):
    size = length(head)
    if head is None or head.next is None:
        return head
    if k >= size:
        k = k % size
    if k == 0:
        return head
    count = size - k
    i = 1
    curr = head
    while i < count:
        curr = curr.next
        i += 1
    head2 = curr.next
    curr.next = None
    tail = head2
    while tail.next != None:
        tail = tail.next
    tail.next = head
    return head2
    




head = takeInput()
k = int(input())
printLL(RotateLL(head, k))























