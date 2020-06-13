#707

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        if index == 0:
            return self.head.val
        elif index == (self.length):
            return self.tail.val
        else:
            node = self.head
            current = 0
            while node is not None:
                if current == index:
                    return node.val
                node = node.next
                current += 1
            return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = newNode
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)

        elif index == self.length:
            self.addAtTail(val)
        else:
            current = 0
            prev = None
            node = self.head
            newNode = Node(val)
            while(current != index and node.next != None):
                prev = Node
                node = node.next
                current += 1
            if current == index:
                prev.next = newNode
                newNode.next = node
                self.length += 1
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            # self.length -= 1
            # return self.head.next
            
            temp = self.head.val
            newHead = self.head.next
            self.head = newHead
            self.length -= 1
            return temp
        else:
            node = self.head
            current = 0
            prev = None
            while current != index and node.next != None:
                prev = node
                node = node.next
                current += 1
            if current == index:
                prev.next = node.next
                self.length -= 1
              


            
        

















            
