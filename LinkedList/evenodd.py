#328



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
def oddEven(head):
    if not head or not head.next:
            return head
        
    odd = head
    even = head.next
    while odd.next and odd.next.next:
        temp = odd.next
        #printLL(temp)
        odd.next = odd.next.next
        #printLL(odd)
        odd = odd.next
        #printLL(odd)
        #printLL(temp)
        #printLL(even)
        temp.next = odd.next
        #printLL(temp)
        #printLL(even)
        
        
    odd.next = even
    
    return head
    
   
head = takeInput()
##printLL(head)


printLL(oddEven(head))









