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


def buildTreePostOrder(postorder,inOrder):
    if len(postorder)==0:
        return None
    rootData = postorder[-1]
    root = BinaryTreeNode(rootData)
    rootIndex = -1
    for i in range(len(inOrder)):
        if(inOrder[i] == rootData):
            rootIndex = i
            break
    # length = len(postorder)
    leftTree = buildTreePostOrder(postorder[:rootIndex], inOrder[:rootIndex])
    rightTree = buildTreePostOrder(postorder[rootIndex: -1], inOrder[rootIndex + 1:])
    root.left=leftTree
    root.right=rightTree
    return root
    
n=int(input())
postorder=[int(z) for z in input().split()]
inorder=[int(f) for f in input().split()]

root=buildTreePostOrder(postorder,inorder)

printLevelWise(root)
#printLevelATNewLine(root)











    








        
