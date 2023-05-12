def findCircleNum(isConnected: list[list[int]]) -> int:
    n = len(isConnected)
    traversed = [False] * n
    answer = 0
    def DFS(i):
        nonlocal traversed
        if traversed[i] is True:
            return
        traversed[i] = True
        for j in range(n):
            if isConnected[i][j] == 1:
                if j != i:
                    DFS(j)
    for i in range(0, n):
        if traversed[i] is False:
            answer += 1
            DFS(i)

    return answer

print(findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))