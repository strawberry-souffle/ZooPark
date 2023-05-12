def subsetsUnique(nums: list[int]):
    def dfs(index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            dfs(i + 1, path + [nums[i]], res)
    res = []
    nums.sort()
    dfs(0, [], res)
    return res

a = subsetsUnique([1,2,2])
print(a)