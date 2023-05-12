def minJump(nums: list[int]) -> int:
    target = len(nums) - 1
    def recurFrom(index, excluding):
        if index >= target:
            return 0
        if index + nums[index] >= target:
            return 1
        best = 0
        bestI = 0
        for i in range(excluding + 1, index + nums[index] + 1):
            if i + nums[i] > best:
                best = i + nums[i]
                bestI = i
        return 1 + recurFrom(bestI, index + nums[index])
    return recurFrom(0, 0)

print(minJump([2,1]))