import random
import math
import time
# manhattanDistance problem example
def solve(n, m, table):
    dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    path = []
    traversed = []

    def solveCell(i, j):
        if table[i][j] == -1:
            return True
        newI = i + dir[table[i][j]][0]
        newJ = j + dir[table[i][j]][1]
        if (i, j) in traversed:
            return False
        if newI < 0 or newI >= n or newJ < 0 or newJ >= m:
            table[i][j] = -1
            path.append((i + 1, j + 1))
            return True
        else:
            traversed.append((i, j))
            while 0 <= newI < n and 0 <= newJ < m:
                if solveCell(newI, newJ) == False:
                    return False
                else:
                    newI += dir[table[i][j]][0]
                    newJ += dir[table[i][j]][1]
            table[i][j] = -1
            path.append((i + 1, j + 1))
            return True

    for i in range(n):
        for j in range(m):
            if table[i][j] != -1:
                solveCell(i, j)

    solved = True
    for i in range(n):
        for j in range(m):
            if table[i][j] != -1:
                print("NO")
                solved = False
                break
        if solved is False:
            break
    if solved is True:
        print("YES")
        for i in path:
            print(i[0], i[1])

def evaluate(points: list[tuple]):
    sum = 0
    for i in range(0, len(points) - 1):
        for j in range(i + 1, len(points)):
            sum += math.fabs(points[i][0] - points[j][0]) + math.fabs(points[i][1] - points[j][1])
    return sum


avgEvTime = 0
avgSolveTime = 0
maxSolveTime = 0
for t in range(10000):
    n = random.randint(10, 100)
    m = random.randint(10, 100)
    points: list[list[int]] = [[random.randint(0,3) for _ in range(m)] for _ in range(n)]

    # start = time.time()
    # evaluation = evaluate(points)
    # avgEvTime += (time.time() - start)

    start = time.time()
    answer = solve(n, m, points)
    avgEvTime += (time.time() - start)
    if (time.time() - start) > maxSolveTime:
        maxSolveTime = (time.time() - start)

    # if evaluation != answer:
    #     print("Fail")
    # else:
    print("Test Completed", t)

print("Average Time Taken For Evaluation:", (avgEvTime / 100))
print("Average Time Taken For Solving:", (avgSolveTime / 100))
print("Maximum Time Taken For Solving:", maxSolveTime)
