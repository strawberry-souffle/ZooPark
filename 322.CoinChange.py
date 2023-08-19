import math


def coinChange(coins: list[int], amount: int) -> int:
    memo = dict()
    memo[0] = 0
    def bigF(s: int):
        if s in memo:
            return memo[s]
        elif s < 0:
            return 100000
        else:
            memo[s] = min(bigF(s - i) for i in coins) + 1
            return memo[s]
    return bigF(amount) if bigF(amount) < 100000 else -1

print(coinChange([186,419,83,408], 6249))