import math
import random
import time


def isHappy(n: int) -> bool:
    met = set()
    def loop(n: int):
        sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum += digit**2
        if sum == 1:
            return True
        elif sum in met or sum == 0:
            return False
        met.add(sum)
        return loop(sum)
    return loop(n)

# Floyd Cycle Detection
def isHappy_alt(n: int) -> bool:
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1

print(isHappy(19))
print(isHappy_alt(19))