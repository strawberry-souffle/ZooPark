nums: list[int] = list[int](input().split())
target = int(input())


def searchRange(self, nums: list[int], target: int) -> list[int]:
    def binarySearch(arr, k):
        def leftSearch(l, r):
            if (r < l):
                return l
            m = (l + r) // 2
            if k == arr[m]:
                return leftSearch(l, m - 1)
            elif arr[m + 1] == k:
                return m + 1
            elif k != arr[m]:
                return leftSearch(m + 1, r)

        def rightSearch(l, r):
            if (l > r):
                return r
            m = (l + r) // 2
            if k == arr[m]:
                return rightSearch(m + 1, r)
            elif arr[m - 1] == k:
                return m - 1
            elif k != arr[m]:
                return rightSearch(l, m - 1)

        def binaryRec(l, r):
            if (l > r):
                return [-1, -1]
            m = (l + r) // 2
            if k == arr[m]:
                return [leftSearch(l, m), rightSearch(m, r)]
            if k < arr[m]:
                return binaryRec(l, m - 1)
            else:
                return binaryRec(m + 1, r)

        ans = binaryRec(0, len(arr) - 1)
        return ans

    return binarySearch(nums, target)