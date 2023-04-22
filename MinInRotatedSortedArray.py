nums: list[int] = [3,4,5,1,2]
def SearchMin(arr):
    def simplifyArr(l,r):
        if l > r:
            return -1
        if arr[l] > arr[r]:
            m = (l + r) // 2
            if arr[m] > arr[r]:
                if arr[m + 1] < arr[r]:
                    return m + 1
                return simplifyArr(m + 1, r)
            else:
                return simplifyArr(l, m)
        else:
            return l
    # def binaryRec(l, r):
    #     if (l > r):
    #         return -1
    #     m = (l + r) // 2
    #     if k == arr[m]:
    #         return m
    #     if k < arr[m]:
    #         return binaryRec(l, m - 1)
    #     else:
    #         return binaryRec(m + 1, r)

    ans = simplifyArr(0, len(arr) - 1)
    return ans

print("aaaaaaaaaa", SearchMin(nums))