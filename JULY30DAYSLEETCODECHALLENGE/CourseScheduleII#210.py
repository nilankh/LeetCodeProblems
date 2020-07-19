#210
#rough page no 63
def findOrder(numCourses, prerequisites):
    global adj
    adj = [[] for i in range(numCourses)]
    for courses in prerequisites:
        adj[courses[1]].append(courses[0])

    global s
    s = []
    global visited
    visited = [0] * numCourses
    for i in range(numCourses):
        if visited[i] == 0 and dfs(i):
            return []
    s.reverse()
    return s
    

def dfs(u):
    visited[u] = 1
    for v in adj[u]:
        if visited[v] == 1:
            return True
        if visited[v] == 0 and dfs(v):
            return True
    visited[u] = 2
    s.append(u)
    return False
        






numCourses = 4
prerequisites = [[1,0],[2, 0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))


















































