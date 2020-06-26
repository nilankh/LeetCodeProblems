#174
import sys
def Dungeon(dungeon):
    if dungeon == None or len(dungeon) == 0 or len(dungeon[0]) == 0:
        return 0
    return DungeonHelper(0, 0, dungeon)

def DungeonHelper(i, j, dungeon):
    if i >= len(dungeon) or j >= len(dungeon[0]):
        return sys.maxsize
    health = min(DungeonHelper(i + 1, j, dungeon), DungeonHelper(i, j + 1, dungeon))
    if health == sys.maxsize:
        health = 1

    res = 0
    if health - dungeon[i][j] > 0:
        res = health - dungeon[i][j]
    else:
        res = 1
    return res
        

s = input().split()
n, m = int(s[0]), int(s[1])
b = input().split()
dungeon = [[int(b[m*i+j]) for j in range(m)] for i in range(n)]
print(Dungeon(dungeon))

