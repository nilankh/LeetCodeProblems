#107
#rough page no 107
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printLevelATNewLine(root):
    if root is None:
        return root
    queue = []
    List = []
    queue.append(root)
    while len(queue) > 0:
        ans = []
        for u in range(len(queue)):
            node = queue.pop(0)
            ans.append(node.data)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        List.append(ans)
    List.reverse()
    return List
    








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
k = printLevelATNewLine(root)
print(k)



































