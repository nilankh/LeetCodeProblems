#129
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

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def sumRootToLeafNumbers(root):
    if not root:
        return 0
    if not root.left and not root.right :
        return int(root.data)
    if root.left:
        
        root.left.data = 10 * root.data + root.left.data
    if root.right:
        
        root.right.data = 10 * root.data + root.right.data
    
    return sumRootToLeafNumbers(root.left) + sumRootToLeafNumbers(root.right)


root=treeInput()
printTree(root)
print(sumRootToLeafNumbers(root))




















