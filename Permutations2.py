def permutationsUnique(nums: list[int]):
    res = []
    def dfs(arr, path):
        global res
        if len(arr) == 1:
            res.append(path + [arr[0]])
        for i in range(0, len(arr)):
            if arr[i] == arr[i-1] and i != 0:
                continue
            dfs(arr[:i] + arr[i + 1:], path + [arr[i]])

    nums.sort()
    dfs(nums, [], res)
    return res

a = permutationsUnique([1,1,2])
print(a)