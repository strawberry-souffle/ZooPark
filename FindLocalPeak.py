import math

nums: list[int] = [1,2,3,1]
def binarySearch(arr):
    if len(arr) == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return len(arr) - 1
    def binaryRec(l, r):
        if(l > r):
            return -1
        m = (l + r) // 2

        if arr[m + 1] > arr[m]:
            return binaryRec(m + 1, r)
        elif arr[m - 1] > arr[m]:
            return binaryRec(l, m - 1)
        else:
            return m
    ans = binaryRec(1, len(arr) - 2)
    return ans
print(binarySearch(nums))
