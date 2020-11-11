#797
#rough page no 67
def allpathSource(input):
    global result
    result = []
    dfs([], 0)
    return result
def dfs(path, u):
    if u == len(input) - 1:
        result.append(path +[u])
    else:
        for v in input[u]:
            dfs(path + [u], v)
        




input = [[1,2], [3], [3], []] 
k = allpathSource(input)
print(k)






