nums: list[int] = [int(x) for x in input().split(",")]
target = int(input())
def binarySearch(arr, k):
    def simplifyArr(l,r):
        if l > r:
            return -1
        if k < arr[l]:
            m = (l + r) // 2
            if arr[m] > arr[r]:
                if arr[m + 1] < arr[r]:
                    return binaryRec(m + 1, r)
                return simplifyArr(m + 1, r)
            else:
                if k > arr[m]:
                    return binaryRec(m, r)
                elif k == arr[m]:
                    return m
                else:
                    return simplifyArr(l, m - 1)
        elif k > arr[l]:
            m = (l + r) // 2
            if arr[m] < arr[l]:
                if arr[m - 1] > arr[l]:
                    return binaryRec(l, m - 1)
                return simplifyArr(l, m - 1)
            else:
                if k < arr[m]:
                    return binaryRec(l, m)
                elif k == arr[m]:
                    return m
                else:
                    return simplifyArr(m + 1, r)
        else:
            return l
    def binaryRec(l, r):
        if (l > r):
            return -1
        m = (l + r) // 2
        if k == arr[m]:
            return m
        if k < arr[m]:
            return binaryRec(l, m - 1)
        else:
            return binaryRec(m + 1, r)

    ans = simplifyArr(0, len(arr) - 1)
    return ans

print(binarySearch(nums, target))