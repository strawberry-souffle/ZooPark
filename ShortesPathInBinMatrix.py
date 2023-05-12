def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    from collections import deque
    m_d = len(grid)
    n_d = len(grid[0])
    target = (m_d - 1, n_d - 1)
    if grid[0][0] == 1 or grid[target[0]][target[1]] == 1:
        return -1
    visited = {(0,0)}
    q = deque()
    q.append((0,0))
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    def addIfValid(m, n, q: deque):
        if 0 <= m < m_d and 0 <= n < n_d and grid[m][n] == 0 and (m, n) not in visited:
            q.append((m, n))
            visited.add((m, n))


    #BFS traversal
    depth = 1
    while len(q) > 0:
        limit = len(q)
        for _ in range(limit):
            m, n = q.popleft()
            if (m, n) == target:
                return depth
            for m_off, n_off in directions:
                addIfValid(m + m_off, n + n_off, q)
        depth += 1

    return -1


print(shortestPathBinaryMatrix([[0,1],[1,0]]))