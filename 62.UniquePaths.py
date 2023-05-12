def uniquePaths(m: int, n: int) -> int:
    calculatedPaths = dict()
    calculatedPaths[tuple((1, 1))] = 1
    def findPathsIn(m, n):
        nonlocal calculatedPaths
        if m == 0 or n == 0:
            return 0
        if m >= n:
            if tuple((m, n)) in calculatedPaths:
                return calculatedPaths[(m, n)]
            else:
                if m == 1 or n == 1:
                    calculatedPaths[(m, n)] = 1
                calculatedPaths[(m, n)] = findPathsIn(m - 1, n) + findPathsIn(m, n -1)
                return calculatedPaths[(m,n)]
        else:
            if tuple((n, m)) in calculatedPaths:
                return calculatedPaths[(n, m)]
            else:
                if m == 1 or n == 1:
                    calculatedPaths[(n, m)] = 1
                calculatedPaths[(n, m)] = findPathsIn(m - 1, n) + findPathsIn(m, n - 1)
                return calculatedPaths[(n, m)]

    return findPathsIn(m , n)

#smart as hell
def uniquePaths_alt(m: int, n: int) -> int:
    grid = [[0] * n for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if row == 0 or col == 0:
                grid[row][col] = 1
            else:
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
    return grid[m - 1][n - 1]

print(uniquePaths(15,15))
