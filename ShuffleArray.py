import random


# O(n^2) - from new array creations
class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.random = random
    def reset(self) -> list[int]:
        return self.nums
    def shuffle(self) -> list[int]:
        def dfs(arr, path):
            if len(arr) == 1:
                return path + [arr[0]]
            i = self.random.randrange(0, len(arr))
            return dfs(arr[:i] + arr[i + 1:], path + [arr[i]])

        return dfs(self.nums, [])

# O(n) - shuffles array in place
class Solution_FisherYates:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array