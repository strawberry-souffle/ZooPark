def longestString(x: int, y: int, z: int) -> int:
    memo = dict()

    def optimalSolution(lastLetter, x, y, z):
        if x < 0 or y < 0 or z < 0:
            return -2
        if (lastLetter, x, y, z) in memo:
            return memo[(lastLetter, x, y, z)]
        else:
            if lastLetter == 'A':
                memo[(lastLetter, x, y, z)] = 2 + optimalSolution('B', x, y - 1, z)
            else:
                memo[(lastLetter, x, y, z)] = 2 + max(optimalSolution('A', x - 1, y, z), optimalSolution('B', x, y, z - 1))
            return memo[(lastLetter, x, y, z)]

    ans = 2 + max(optimalSolution('A', x - 1, y, z), optimalSolution('B', x, y - 1, z), optimalSolution('B', x, y, z - 1))
    return ans


print(longestString(2, 5, 1))
