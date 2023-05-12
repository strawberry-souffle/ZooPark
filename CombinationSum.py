def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    output = []
    n = len(candidates)
    def dfs(arr: list[int], index, target):
        nonlocal output
        if index >= n:
            return
        while target > 0:
            dfs(arr.copy(), index + 1, target)
            arr += [candidates[index]]
            target -= candidates[index]
        if target == 0:
            output.append(arr)
    dfs([], 0, target)
    return output

# somehow not faster than previous
def combinationSum_alt(candidates: list[int], target: int) -> list[list[int]]:
    output = []
    n = len(candidates)
    def dfs(arr: list[int], index, target):
        nonlocal output
        if index >= n:
            return
        i = 0
        while target > 0:
            dfs(arr, index + 1, target)
            arr.append(candidates[index])
            target -= candidates[index]
            i += 1
        if target == 0:
            output.append(arr.copy())
        del arr[-i:]
    dfs([], 0, target)
    return output

print(combinationSum_alt([2,3,6,7], 7))

