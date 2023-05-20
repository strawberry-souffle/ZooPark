def numberOfArithmeticSlices(nums: list[int]) -> int:
    diff = [0] * len(nums)
    for i in range(1, len(nums)):
        diff[i] = nums[i] - nums[i - 1]

    i = 1
    j = 2
    output = 0
    while j < len(nums):
        if diff[j] == diff[i]:
            if j - i >= 1:
                output += j - i
            j += 1
        else:
            i = j
            j += 1
    return output

print(numberOfArithmeticSlices([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))