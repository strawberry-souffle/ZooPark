def canJump(nums: list[int]) -> bool:
    accumulated = nums[0]
    for i in range(1, len(nums)):
        if accumulated > 0:
            accumulated = max(accumulated - 1, nums[i])
        else:
            return False
    return True

print(canJump([3,2,1,0,4]))
