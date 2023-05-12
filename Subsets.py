def subsets1(nums: list[int]):
    def dfs(index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]], res)
    res = []
    dfs(0, [], res)
    return res


a = subsets1([1,2,3,4,5])
print(a)
