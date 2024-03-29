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
    
    #finding left and right preOrder
    # leftPreorder = preOrder[1:lenleftSubtree + 1]
    # rightPreOrder = preOrder[lenleftSubtree + 1:]
    
    

    # Calling recursion on both left and right with finding preOrder of both left and right    
    leftChild=buildTreePreOrder(preOrder[1:left+1],leftIn)
    rightChild=buildTreePreOrder(preOrder[left+1:],rightIn)
    root.left=leftChild
    root.right=rightChild
    return root

n=int(input())
preorder=[int(z) for z in input().split()]
inorder=[int(f) for f in input().split()]
root=buildTreePreOrder(preorder,inorder)
printLevelWise(root)
#printLevelATNewLine(root)




