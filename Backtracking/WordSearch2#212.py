#212
#pagno43
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

    def insert(self, word):
        curr = self
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.endOfWord = True
    
def findWords(board, words):
    if len(words) == 0: return []
    trie = TrieNode()
    for w in words:
        trie.insert(w)
    result = set()#koi duplicate word na aaye islia set consider kr rhe h
    
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board,i, j, trie, "", result)
    result_v = list(result)
    return result_v

def dfs(board, i, j, trie, s, result):
    c = board[i][j]
    if c == '$': return
    board[i][j] = '$'
    t = trie.children[ord(c) - ord('a')]
    if(t != None):
        ss = s + c
        if t.endOfWord: result.add(ss)
        if i < len(board) - 1: dfs(board, i + 1, j, t, ss, result)
        if j < len(board[0])-1: dfs(board, i, j + 1, t, ss, result)
        if i < 0: dfs(board, i - 1, j, t, ss, result)
        if j > 0: dfs(board, i, j - 1, t, ss, result)
    board[i][j]=c   

    
    
    
r = input().split()
b = r[2:]
board = [[ b[int(r[1])*i+j] for j in range(int(r[1])) ] for i in range(int(r[0]))]
##print(board)
words = ["oath","pea","eat","rain"]
k = findWords(board, words)
print(*k)








       
