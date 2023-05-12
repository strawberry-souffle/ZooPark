import time


def rob(nums: list[int]) -> int:
    n = len(nums)
    if n <= 3:
        return max(nums)
    buffer = [-1] * n
    def robHouse(index, start):
        if index >= start - 1:
            return 0

        if buffer[index] != -1:
            return buffer[index]

        buffer[index] = nums[index] + max(robHouse(index + 2, start), robHouse(index + 3, start))
        return buffer[index]

    answer1 = robHouse(-n, 0)
    buffer = [-1] * n
    answer2 = robHouse(-n + 1, 1)
    buffer = [-1] * n
    answer3 = nums[-1] + robHouse(-n + 2, -1)
    return max(answer1, answer2, answer3)

def rob_alt(nums: list[int]) -> int:
    if len(nums) <= 3:
        return max(nums)
    def robArr(arr: list[int]):
        best = [-1] * len(arr)
        def calculateBest(index):
            nonlocal best
            if best[index] != -1:
                return best[index]
            if index < 0:
                best[index] = 0
                return best[index]
            best[index] = max(calculateBest(index - 1), arr[index] + calculateBest(index - 2))
            return best[index]
        return calculateBest(len(arr) - 1)
    def robArr_alt(arr: list[int]):
        prev = arr[0]
        prePrev = 0
        for i in range(1, len(arr)):
            tmp = max(arr[i] + prePrev, prev)
            prePrev = prev
            prev = tmp
        return prev

    return max(robArr_alt(nums[1:]), robArr_alt(nums[:-1]))

print(rob_alt([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]))