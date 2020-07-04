#79
def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(board, i, j, 0, word):
                return True
    return False
def dfs(board, i, j, count, word):
    if count == len(word):
        return True
    if(i == -1 or i == len(board) or j == -1 or j == len(board[0]) or board[i][j] != word[count]):
        return False
    temp = board[i][j]
    board[i][j] = '*'
    found = dfs(board, i + 1, j, count + 1, word) or dfs(board, i - 1, j, count + 1, word) or dfs(board, i, j + 1, count + 1, word) or dfs(board, i, j - 1, count + 1, word)
    board[i][j] = temp
    return found

#board =[['A','N','S','Q'],['S','O','L','R'],['K','T','O','G']]
r = input().split()
b = r[2:]
board = [[ b[int(r[1])*i+j] for j in range(int(r[1])) ] for i in range(int(r[0]))]
#print(board)
##word = "SOLE"
word = input()
print(exist(board, word))


