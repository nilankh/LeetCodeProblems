#130
def surroundedRegions(board):
    r = len(board)
    if r <= 2:
        return
    c = len(board[0])
    if c <= 2:
        return
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O' and (i == 0 or i == r - 1 or j == 0 or j == c - 1):
                dfs(board, i, j)

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'A':
                board[i][j] = 'O'
            
    return board  
def dfs(board, i, j):
    r = len(board)
    c = len(board[0])
    if i >= 0 and i < r and j >= 0 and j < c and board[i][j] == 'O' :
            board[i][j] = 'A'
            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)
    

s = input().split()
n, m = int(s[0]), int(s[1])
b = input().split()
board = [[b[m*i+j] for j in range(m)] for i in range(n)]
k = surroundedRegions(board)
print(k)






