arr: list[int] = [2,3,1,2,4,3]
finding = 7
def numSubarraySumMoreThanK(nums: list[int], k: int) -> int:
    window = nums[0]
    l = 0
    r = 0
    out = len(nums) + 1
    if k < 1:
        return 0
    while r < len(nums):
        if window < k:
            if r + 1 < len(nums):
                r += 1
                window += nums[r]
            else:
                break
        else:
            while window >= k:
                if (r - l + 1) < out:
                    out = (r - l + 1)
                window -= nums[l]
                l += 1
    if out <= len(nums):
        return out
    return 0
print(numSubarraySumMoreThanK(arr, finding))