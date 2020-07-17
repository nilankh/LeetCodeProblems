#147
#page53 leetcode set

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
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count
#this will give TLE error
def insertionSort(head):
    curr = head
    insertionPointer = head
    curr = curr.next
    while(curr != None):
        insertionPointer = head
        while(insertionPointer != curr):
            if insertionPointer.data > curr.data:
                temp = curr.data
                curr.data = insertionPointer.data
                insertionPointer.data = temp
            else:
                insertionPointer = insertionPointer.next
                
        curr = curr.next
    return head
def insertionSortRevised(head):
    if head is None:
        return head
    dummy = Node(0)
    #print(dummy.data)
    pre = dummy
    nextt = None
    curr = head
    while curr != None:
        nextt = curr.next
        while pre.next != None and pre.next.data < curr.data :
            pre = pre.next
        curr.next = pre.next
        pre.next = curr
        pre = dummy
        curr = nextt
    return dummy.next
head = takeInput()
printLL(head)
printLL(insertionSortRevised(head))








                
    








