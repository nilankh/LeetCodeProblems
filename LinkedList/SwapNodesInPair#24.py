#24





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data) + " -> ",end = "")
        head = head.next
    print("None")
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

def swapNodesInPairs(head):
    if head is None or head.next is None:
        return head
    p = head
    newStart = p.next
    while(True):
        q = p.next
        temp = q.next
        q.next = p
        if temp == None or temp.next == None:
            p.next = temp
            break
        p.next = temp.next
        p = temp
    return newStart
##    count = 1
##    prev = None
##    curr = head
##    while(curr != None and count < 2):
##        prev = curr
##        curr = curr.next
##        count += 1
##    if curr!= None:
##        T = curr.next
##        curr.next = prev
##        prev.next = T
##    return curr
        
        
        
def swapNodesInPairsR(head):
    if head and head.next:
        temp = head.next
        head.next = swapNodesInPairsR(temp.next)
        temp.next = head
        return temp
    return head

head = takeInput()
printLL(swapNodesInPairsR(head))















