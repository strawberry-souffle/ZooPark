import math
import bisect
# classic brute-force-like DP, O(n^2)
def lengthOfLIS(nums: list[int]) -> int:

    n = len(nums)
    dp = [0] * n
    def findDP(i):
        if dp[i] != 0:
            return dp[i]
        else:
            seq = [(findDP(j) if nums[j] < nums[i] else 0) for j in range(0, i)]
            if len(seq) > 0:
                dp[i] = max(seq) + 1
            else:
                dp[i] = 1
            return dp[i]
    return max(findDP(i) for i in range(0, n))

# insane intuition. tails[i] - last element of tail whose length is i + 1; binarySearchM - finds smallest element more or equal to target. -1 ~ no elements satisfying the condition
# Encountering a new element we look into where we can insert it. Changing value of tails[i] does not affect properties of tails[i + 1]
# O(nlog(n))
def lengthOfLIS_alt(nums: list[int]) -> int:
    tails = [nums[0]]
    for i in nums:
        indexToSubstitute = bisect.bisect_left(tails, i)
        if indexToSubstitute >= len(tails):
            tails.append(i)
        else:
            tails[indexToSubstitute] = i
    return len(tails)

# print(lengthOfLIS_alt([10,9,2,5,3,7,101,18]))
print(bisect.bisect_left([0,1,3,5], 3))
