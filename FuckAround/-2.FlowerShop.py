import random
import math
import time
def solve(k, flowers: list[int]):
    def subtractFromList(list_, subtracting, startIndex, endIndex):
        for i in range(startIndex, endIndex):
                list_[i] -= subtracting
    # def recurDown(flowers):
    #     flowers = [i for i in flowers if i > 0]
    #     if len(flowers) < k:
    #         return 0
    #     else:
    #         sum = 0
    #         n = len(flowers)
    #         for i in range(0, (len(flowers)//k)):
    #             subtracting = min(flowers[k * i:k * (i + 1)])
    #             if subtracting > 0:
    #                 sum += subtracting
    #                 subtractFromList(flowers, subtracting, k * i, k * (i + 1))
    #             else:
    #                 break
    #         return sum + recurDown(flowers)
    # return recurDown(flowers)
    sum = 0
    while len(flowers) >= k:
        for i in range(0, len(flowers)//k):
            subtracting = min(flowers[k * i:k * (i + 1)])
            if subtracting > 0:
                sum += subtracting
                subtractFromList(flowers, subtracting, k * i, k * (i + 1))
            else:
                break
        flowers = [i for i in flowers if i > 0]
    return sum

def evaluate(k, flowers: list[int]):
    def recurDown(flowers):
        if len(flowers) < k:
            return 0
        for i in range(0, k):
            flowers[i] -= 1
        return 1 + recurDown([i for i in flowers if i > 0])
    return recurDown(flowers)


# n, k = map(int, input().split())
# a = [int(x) for x in input().split()]
# print(solve(k, a))
# print(a)

avgEvTime = 0
avgSolveTime = 0
maxSolveTime = 0
for t in range(100):
    n = random.randint(10, 15)
    k = random.randint(5, n)
    flowers: list[int] = [(random.randrange(1, 10)) for _ in range(n)]

    start = time.time()
    evaluation = evaluate(k, flowers.copy())
    avgEvTime += (time.time() - start)

    start = time.time()
    answer = solve(k, flowers.copy())
    avgEvTime += (time.time() - start)
    if (time.time() - start) > maxSolveTime:
        maxSolveTime = (time.time() - start)

    if evaluation != answer:
        print("Fail")
    else:
        print("Test Completed", t)

print("Average Time Taken For Evaluation:", (avgEvTime / 100))
print("Average Time Taken For Solving:", (avgSolveTime / 100))
print("Maximum Time Taken For Solving:", maxSolveTime)