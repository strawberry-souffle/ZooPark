def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    output = []
    n = len(candidates)
    candidates.sort()
    # prev is a workaround, try substituting it with arr[1] and run candidates = [2,5,2,1,2], target = 8 on it
    def dfs(arr: list[int], index, target, prev):
        nonlocal output
        if index >= n or target <= 0:
            return
        if index == 0 or candidates[index] != candidates[index - 1] or candidates[index] == prev:
            dfs(arr, index + 1, target, -1)
            arr.append(candidates[index])
            target -= candidates[index]
            dfs(arr, index + 1, target, candidates[index])
            if target == 0:
                output.append(arr.copy())
            arr.pop(-1)
        else:
            dfs(arr, index + 1, target, prev)
    dfs([], 0, target, -1)
    return output

# now that's smarter, and faster
def combinationSum2_alt(candidates: list[int], target: int) -> list[list[int]]:
    output = []
    elements = []
    dict = {}
    for item in candidates:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
            elements.append(item)
    n = len(elements)
    def dfs(arr: list[int], index, target):
        nonlocal output
        if target == 0:
            output.append(arr)
            return
        if index >= n or target < 0:
            return
        for i in range(1, dict[elements[index]] + 1):
            newT = target - (elements[index] * i)
            if newT < 0:
                break
            dfs(arr + ([elements[index]] * i), index + 1, newT)
        dfs(arr, index + 1, target)

    dfs([], 0, target)
    return output

# idk who claims previous one to be smart. This one is cleaner and faster. Works similar to Subsets2
def combinationSum2_altalt(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    n = len(candidates)
    output = []

    def dfs(arr: list[int], index, target):
        nonlocal output
        if target == 0:
            output.append(arr.copy())
            return
        if target < 0:
            return
        for i in range(index, n):
            if candidates[i] > target:
                break
            if candidates[i] == candidates[i - 1] and i > index:
                continue
            arr.append(candidates[i])
            dfs(arr, i + 1, target - candidates[i])
            arr.pop()

    dfs([], 0, target)
    return output

print(combinationSum2_alt([10,1,2,7,6,1,5], 8))