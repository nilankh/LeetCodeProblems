#1367


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printTree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)
def takeInput():
    inputList=[int(ele) for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next=newNode
            tail=newNode
    return head


def takeInputOfBT():
    rootData=int(input())
    if rootData == -1:
        return None

    root=BinaryTreeNode(rootData)
    leftTree=takeInput()
    rightTree=takeInput()
    root.left=leftTree
    root.right=rightTree
    return root

root=takeInputOfBT()
printTree(root)















