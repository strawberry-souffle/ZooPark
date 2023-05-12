arr: list[int] = [10,5,2,6]
finding = 100
def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    window = nums[0]
    l = 0
    r = 0
    out = 0
    if k <= 1:
        return 0
    while l < len(nums) and r < len(nums):
        if window < k:
            out += r - l + 1
            if r + 1 < len(nums):
                r += 1
                window *= nums[r]
            else:
                break
        else:
            window /= nums[l]
            l += 1
    return out
print(numSubarrayProductLessThanK(arr, finding))