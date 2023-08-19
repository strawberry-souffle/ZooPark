# DP approach
def integerBreak(n: int) -> int:
    memo = dict()
    memo[1] = 1
    memo[2] = 1
    memo[3] = 2
    memo[4] = 3
    memo[5] = 4
    memo[6] = 6
    if n in memo:
        return memo[n]
    memo[1] = 1
    memo[2] = 2
    memo[3] = 3
    memo[4] = 4
    memo[5] = 5
    memo[6] = 6

    def bigF(s):
        nonlocal memo
        if s in memo:
            return memo[s]
        else:
            memo[s] = max((i * bigF(s - i)) for i in range(1, s))
            return memo[s]

    return bigF(n)


# O(1) using math properties. We need to maximize number of 3's, as it yields the greatest product
def integerBreak_alt(n: int) -> int:
    if n <= 3:
        return n - 1
    elif n % 3 == 0:  # 3+...+3
        return 3 ** (n // 3)
    elif n % 3 == 1:  # 3+...+3+2+2
        return 3 ** ((n // 3) - 1) * 4
    else:  # 3+...+3+2
        return 3 ** (n // 3) * 2


print(integerBreak_alt(10))
