def numIslands(grid: list[list[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    traversed = [([False] * n) for _ in range(m)]
    answer = 0

    def traverseIsland(x, y):
        nonlocal traversed
        if x < 0 or y < 0 or x >= m or y >= n or traversed[x][y] is True or grid[x][y] == "0":
            return False
        traversed[x][y] = True
        traverseIsland(x, y + 1)
        traverseIsland(x, y - 1)
        traverseIsland(x - 1, y)
        traverseIsland(x + 1, y)
        return True

    for x in range(0, m):
        for y in range(0, n):
            if grid[x][y] == "0":
                continue
            if traverseIsland(x, y) is True:
                answer += 1

    return answer

print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))