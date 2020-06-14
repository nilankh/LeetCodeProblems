#1019



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

#the code is fully correct but it will not work
#longer inputs so tle error will show
##def nextLargerNodes(head):
##    curr = head
##    Next = curr.next
##    arr = []
##    while curr != None:
##        while Next is not None:
##            if curr.data < Next.data:
##                arr.append(Next.data)
##                curr = curr.next
##                if curr.next is not None:
##                    
##                    Next = curr.next
##                else:
##                    break
##            else:
##                Next = Next.next
##        arr.append(0)
##        if curr.next is not None:
##            curr = curr.next
##        
##            Next = curr.next
##        else:
##            break
##        
##    return arr
def nextLargerNodes(head):
    arr = []
    current = head
    while current:
        arr.append(current.data)
        current = current.next
    #print("arr", arr)
    stack = []
    result = [0] * len(arr)
    for i in range(len(arr)):
        #print("i", i)
        while stack and (arr[stack[len(stack) - 1]] < arr[i]):
            #print("false")
            result[stack.pop()] = arr[i]
            #print("result", result)
        #print("Appended", i)
        stack.append(i)
        #print("Stack", stack)
    return result
head = takeInput()
#printLL(head)
k = nextLargerNodes(head)
print(*k)









