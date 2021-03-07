import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printLevelWise(root):
    if root==None:
        return
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        curr=q.get()
        print(curr.data,end=":")
        if curr.left!=None:
            print("L",end=":")
            print(curr.left.data,end=",")
            q.put(curr.left)
        else:
            print("L:-1,",end="")
        if curr.right!=None:
            print("R",end=":")
            print(curr.right.data,end="")
            q.put(curr.right)
        else:
            print("R:-1",end="")
        print()


def buildTreePreOrder(preOrder,inOrder):
    if len(preOrder)==0:
        return None
    # as we know 0th index of preOrder is our root
    rootData=preOrder[0]
    root=BinaryTreeNode(rootData)
    rootIndex=-1
    # Searching root value in preOder
    for i in range(len(inOrder)):
        if(inOrder[i]==rootData):
            rootIndex=i
            break
    if rootIndex==-1:
        return None
    # leftInoder
    leftIn=inOrder[:rootIndex]
    # rightInorder
    rightIn=inOrder[rootIndex+1:]
    # finding length of elements in leftIn so that we can understand that how many elements in left preoder
    left=len(leftIn)
    # Calling recursion on both left and right with finding preOrder of both left and right
    leftChild=buildTreePreOrder(preOrder[1:left+1],leftIn)
    rightChild=buildTreePreOrder(preOrder[left+1:],rightIn)
    root.left=leftChild
    root.right=rightChild
    return root
'''
def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ'''
n=int(input())
preorder=[int(z) for z in input().split()]
inorder=[int(f) for f in input().split()]
root=buildTreePreOrder(preorder,inorder)
printLevelWise(root)
#printLevelATNewLine(root)




'''
def index(arr,data):
    count=0
    if len(arr)==0:
        return count
    for i in arr:
        if i!=data:
            count+=1
        else:
            return count
            
def buildTreePreOrder(preorder, inorder):
    if len(preorder)==0 and len(inorder)==0:
        return None
    root=BinaryTreeNode(preorder[0])
    i=index(inorder,preorder[0])
    leftarr=preorder[1:i+1]
    rightarr=preorder[i+1:]
    leftin=inorder[:i]
    rightin=inorder[i+1:]
    root.left=buildTreePreOrder(leftarr,leftin)
    root.right=buildTreePreOrder(rightarr,rightin)
    return root

#by manjeetSir
'''






    








        
