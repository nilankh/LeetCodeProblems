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
    left, right = head, head
    stop = False

    #ye line kb chalega??
    def recurseAndReverse(right, m, n):
        nonlocal left, stop
        if(n == 1):
            return
        right = right.next
        if m > 1:
            left = left.next

        recurseAndReverse(right, m - 1, n - 1)

        if left == right or right.next == left:
            stop = True
        if not stop:
            left.data, right.data = right.data, left.data

            left = left.next

    #jb ye call krega tb ye line chalega
    recurseAndReverse(right, m, n)
    return head
    
#isme backtracking use kr rhe h n data change kr rhe h mtlb jaise array me swap krte the na waise hi

head = takeInput()
m = int(input())
n = int(input())
printLL(reverseBetween(head, m, n))












