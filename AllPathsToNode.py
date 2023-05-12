# somehow faster
def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    paths = []
    target = len(graph) - 1
    def DFS(nodeIndex, traversedPath: tuple):
        for i in graph[nodeIndex]:
            if i == target:
                paths.append(traversedPath + (i,))
            else:
                DFS(i, traversedPath + (i,))
    DFS(0, (0,))
    return paths

def allPathsSourceTarget_alt(graph: list[list[int]]) -> list[list[int]]:
    paths = []
    target = len(graph) - 1
    def DFS(nodeIndex, traversedPath: list[int]):
        if nodeIndex == target:
            paths.append(traversedPath + [nodeIndex])
        traversedPath.append(nodeIndex)
        for i in graph[nodeIndex]:
            DFS(i, traversedPath)
        traversedPath.pop(-1)
    DFS(0, [])
    return paths

print(allPathsSourceTarget_alt([[4,3,1],[3,2,4],[3],[4],[]]))