import math
import random
import time
# n = int(input())
# xPoints = [0] * n
# yPoints = [0] * n
# for i in range(n):
#     xPoints[i], yPoints[i] = map(int, input().split())

def manhattanDistance(xPoints: list[int], yPoints: list[int]):
    xPoints.sort()
    yPoints.sort()
    sum = 0
    lastDistSum = xPoints[1] - xPoints[0]
    sum += lastDistSum
    for i in range(2, len(xPoints)):
        dist = xPoints[i] - xPoints[i - 1]
        lastDistSum += (dist * (i - 1)) + dist
        sum += lastDistSum
    lastDistSum = yPoints[1] - yPoints[0]
    sum += lastDistSum
    for i in range(2, len(yPoints)):
        dist = yPoints[i] - yPoints[i - 1]
        lastDistSum += (dist * (i - 1)) + dist
        sum += lastDistSum
    return sum

def manhattanDistanceTest(points: list[tuple]):
    sum = 0
    for i in range(0, len(points) - 1):
        for j in range(i + 1, len(points)):
            sum += math.fabs(points[i][0] - points[j][0]) + math.fabs(points[i][1] - points[j][1])
    return sum


# print(manhattanDistance(xPoints, yPoints))


for t in range(1):
    n = random.randint(100000, 1000000)
    points: list[tuple] = [tuple((random.randrange(0, 100), random.randrange(0, 100))) for _ in range(n)]

    # start = time.time()
    # test = manhattanDistanceTest(points)
    # print("Time to calculate evaluation:", time.time() - start)

    start = time.time()
    answer = manhattanDistance([point[0] for point in points], [point[1] for point in points])
    print("Time to calculate answer:", time.time() - start)

    if test != answer:
        print("Fail")
    else:
        print("Test Completed", t)