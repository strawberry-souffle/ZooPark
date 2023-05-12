from collections import deque


def solve(board: list[list[str]]) -> None:
    m = len(board)
    n = len(board[0])
    last = m - 1
    nLast = n - 1
    preserve = [([False] * n) for _ in range(m)]

    def traverseCell(x, y):
        if x < 0 or y < 0 or x >= m or y >= n or board[x][y] == "X" or preserve[x][y]:
            return
        preserve[x][y] = True
        traverseCell(x, y + 1)
        traverseCell(x, y - 1)
        traverseCell(x - 1, y)
        traverseCell(x + 1, y)
    for i in range(n):
        if board[0][i] == "O":
            traverseCell(0, i)
        if board[last][i] == "O":
            traverseCell(last, i)
    for i in range(1, last):
        if board[i][0] == "O":
            traverseCell(i, 0)
        if board[i][nLast] == "O":
            traverseCell(i, nLast)
    for i in range(1,last):
        for j in range(1,nLast):
            if preserve[i][j] == False:
                board[i][j] = "X"

brd = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(brd)
print("a")