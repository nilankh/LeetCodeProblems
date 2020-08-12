#987
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#according to codinNinjas
def printLevelATNewLineC(root):
    if root == None:
        return
    q1 = queue.Queue()
    q2 = queue.Queue()
    q1.put(root)
    while not q1.empty():
        while not q1.empty():
            curr = q1.get()
            print(curr.data, end = ' ')
            if curr.left != None:
                q2.put(curr.left)
            if curr.right != None:
                q2.put(curr.right)
        q1, q2 = q2, q1
        print()


def verticalOrder(root):
    



def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
#n=int(input())
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelATNewLineC(root)







































        
