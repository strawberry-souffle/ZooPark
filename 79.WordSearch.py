from collections import defaultdict, Counter


def exist(board: list[list[str]], word: str) -> bool:
    rows = len(board)
    columns = len(board[0])
    directions = [(1,0), (-1, 0), (0,1), (0,-1)]
    traversedPatterns = set()
    def dfs(m, n, index, traversed):
        if index == len(word) - 1:
            return True
        output: bool = False
        for m_d, n_d in directions:
            newM = m + m_d
            newN = n + n_d
            if 0 <= newM < rows and 0 <= newN < columns:
                if board[newM][newN] == word[index + 1] and (m, n, newM, newN) not in traversedPatterns:
                    if (newM, newN) not in traversed:
                        traversed.append((newM, newN))
                        traversedPatterns.add((m, n, newM, newN))
                        output = output or dfs(newM, newN, index + 1, traversed)
                        traversed.pop(-1)
                    else:
                        for i in reversed(range(len(traversed) - 1)):
                            if traversed[i] == (newM, newN):
                                break
                            else:
                                traversedPatterns.discard((traversed[i] + traversed[i + 1]))
        return output
    for m in range(rows):
        for n in range(columns):
            if board[m][n] == word[0]:
                if dfs(m, n, 0, [(m,n)]) is True:
                    return True
    return False
def exist_alt(board: list[list[str]], word: str) -> bool:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def dfs(m, n, index):
        if m < 0 or n < 0 or m >= len(board) or n >= len(board[0]) or index >= len(word) or word[index] != board[m][n]:
            return False
        if index == len(word) - 1:
            return True
        for x, y in directions:
            tmp = board[m][n]
            board[m][n] = -1

            if dfs(m + x, n + y, index + 1):
                return True

            board[m][n] = tmp


    # boardDic = defaultdict(int)
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         boardDic[board[i][j]] += 1
    #
    # wordDic = Counter(word)
    # for c in wordDic:
    #     if c not in boardDic or boardDic[c] < wordDic[c]:
    #         return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True

    return False




print(exist_alt([], ""))


