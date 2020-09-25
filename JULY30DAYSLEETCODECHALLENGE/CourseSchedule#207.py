#207
#rough page 60
import collections
def canFinish(numCourses, prerequisites):
    indegree = collections.defaultdict(set)
    outdegree = collections.defaultdict(set)
    for x, y in prerequisites:
        outdegree[y].add(x)
        indegree[x].add(y)

    connection_removed = 0
    indegree_zero = []
    for i in range(numCourses):
        if not indegree[i]:
            indegree_zero.append(i)
            connection_removed += 1
    while indegree_zero:
        node = indegree_zero.pop()
        for x in outdegree[node]:
            indegree[x].remove(node)
            if not indegree[x]:
                indegree_zero.append(x)
                connection_removed += 1
    return connection_removed == numCourses



"""
0--> unvisited
1--> beign Visited
2--> completely visited
"""
def canFinish2ndMethod(numCourses, prerequisites):
    global adj
    adj = [None] * numCourses
    for i in range(numCourses):
        adj[i] = []
    for pre in prerequisites:
        adj[pre[0]].append(pre[1])

    global visited 
    visited = [0] * numCourses
    for i in range(numCourses):
        if visited[i] == 0 and not dfs(i):
            return False
    return True
def dfs(v):
    if visited[v] == 1:
        return False
    visited[v] = 1
    for ad in adj[v]:
        if not dfs(ad):
            return False
    visited[v] = 2
    return True
    
  

numCourses = 2
prerequisites = [[1,0],[0,1]]

# print(canFinish(numCourses, prerequisites))
#visited = [0] * numCourses
print(canFinish2ndMethod(numCourses, prerequisites))





