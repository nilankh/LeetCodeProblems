#92

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

def reverseBetween(head, m, n):
    if head is None:
        return None

    curr = head
    prev = None
    while m > 1:
        prev = curr
        curr = curr.next
        m = m - 1
        n = n - 1
    tail = curr
    conn = prev

    #Iteratively reversiding the nodes until n becomes 0
    
    while n:
        Next = curr.next
        curr.next = prev
        prev = curr
        curr = Next
        n -= 1

    if conn:
        conn.next = prev
    else:
        head = prev
    tail.next = curr
    return head
            
    

head = takeInput()
m = int(input())
n = int(input())
printLL(reverseBetween(head, m, n))












