#208

class TreeNode:

    def __init__(self, v):
        self.val = v
        self.children = {}
        self.endhere = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    def insert(self, word):
        """
        Insert a word into the trie.
        :type word: str
        :rtype: void
        """
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i == len(word) - 1:
                parent.endhere = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.endhere

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix
        :type prefix: str
        :rtype: bool
        """

        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True

obj = Trie()
obj.insert("abc")
obj.insert("mno")
obj.insert("xyz")
obj.insert("mnp")
param2 = obj.search("abc")
print(param2)
param3 = obj.startsWith("ab")
print(param3)
param3 = obj.startsWith("abf")
print(param3)








    
















                
