def productExceptSelf(nums: list[int]) -> list[int]:
    window = 1
    zeroWindow = 1
    zeroIndex = 0
    for i in nums:
        window *= i
        if i == 0 and zeroIndex < 1:
            zeroIndex += 1
        else:
            zeroWindow *= i
    return [int(window / i) if i != 0 else zeroWindow for i in nums]

# Just a Proof Of Concept
def productExceptSelf_NoDiv(nums: list[int]) -> list[int]:
    leftHash = [nums[0]] * len(nums)
    for i in range(1, len(nums)):
        leftHash[i] = leftHash[i-1] * nums[i]
    rightHash = [nums[-1]] * len(nums)
    for i in reversed(range(0, len(nums) - 1)):
        rightHash[i] = rightHash[i+1] * nums[i]
    return [rightHash[1]] + [leftHash[i-1]*rightHash[i + 1] for i in range(1, len(nums) - 1)] + [leftHash[-2]]

# OptimizedOne
def productExceptSelf_NoDiv_alt(nums: list[int]) -> list[int]:
    length = len(nums)
    sol = [1] * length
    pre = 1
    post = 1
    for i in range(length):
        sol[i] *= pre
        pre = pre * nums[i]
        sol[length - i - 1] *= post
        post = post * nums[length - i - 1]
    return (sol)