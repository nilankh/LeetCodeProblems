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

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))
