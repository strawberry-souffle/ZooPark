import math
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
    def binarySearchM(arr, target):
        def binaryRec(start, end):
            if start == end:
                return start
            m = (start + end) // 2
            if arr[m] == target:
                return m
            if target > arr[m]:
                return binaryRec(m + 1, end)
            else:
                return binaryRec(start, m)

        if arr[0] >= target:
            return 0
        if arr[-1] < target:
            return -1
        else:
            return binaryRec(0, len(arr) - 1)

    n = len(nums)
    tails = [nums[0]]
    for i in nums:
        ind = binarySearchM(tails, i)
        if ind == -1:
            tails.append(i)
        else:
            tails[ind] = i
    return len(tails)

print(lengthOfLIS_alt([10,9,2,5,3,7,101,18]))
