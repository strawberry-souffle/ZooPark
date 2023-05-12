x, y, z = map(int, input().split())
max_ = max(x,y,z)
answer = 0
answer += (max_ - x) // 5
x += 5 * ((max_ - x) // 5)
answer += (max_ - y) // 5
y += 5 * ((max_ - y) // 5)
answer += (max_ - z) // 5
z += 5 * ((max_ - z) // 5)

bestSolution = (max_ - x) + (max_ - y) + (max_ - z)
curDistr = [(max_ - x), (max_ - y), (max_ - z)]
def bruteForce(distr, depth):
    global bestSolution
    if depth >= bestSolution:
        return
    if distr[0] == distr[1] == distr[2]:
        bestSolution = depth
    for i in range(3):
        newDistr = distr.copy()
        newDistr[i] -= 1
        bruteForce(newDistr, depth + 1)
        newDistr = distr.copy()
        newDistr[i] -= 5
        bruteForce(newDistr, depth + 1)

bruteForce(curDistr, 0)
answer += bestSolution
print(answer)