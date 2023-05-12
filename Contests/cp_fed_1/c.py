dir = [(0,1), (-1,0), (0,-1), (1,0)]
n, m = map(int, input().split())
table = [[0]] * n
for i in range(n):
    table[i] = [int(x) for x in input()]

path = []
traversed = []
def solveCell(i, j):
    if table[i][j] == -1:
        return True
    newI = i + dir[table[i][j]][0]
    newJ = j + dir[table[i][j]][1]
    if newI < 0 or newI >= n or newJ < 0 or newJ >= m:
        table[i][j] = -1
        path.append((i + 1, j + 1))
        return True

    if (i, j) in traversed:
        return False

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

solved = True
for i in range(n):
    for j in range(m):
        if solveCell(i, j) is False:
            print("NO")
            solved = False
            break
    if solved is False:
        break

# for i in range(n):
#     for j in range(m):
#         if table[i][j] != -1:
#             print("NO")
#             solved = False
#             break
#     if solved is False:
#         break
if solved is True:
    print("YES")
    for i in path:
        print(i[0],i[1])



