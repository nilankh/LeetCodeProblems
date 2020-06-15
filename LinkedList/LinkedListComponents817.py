#817

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

def LinkedListComponents(head, G):
    count = 0
    temp = head
    while temp:
        if temp.data in G:
            count += 1
            while temp and temp.data in G:
                temp = temp.next
        else:
            temp = temp.next
    return count


head = takeInput()
G = [int(x) for x in input().split()]
print(LinkedListComponents(head, G))
##printLL(head)












