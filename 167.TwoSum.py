def twoSum(numbers: list[int], target: int) -> list[int]:
    j = len(numbers) - 1
    i = 0
    while i < len(numbers) and j >= 0:
        sum_ = numbers[i] + numbers[j]
        if sum_ == target:
            return [i + 1, j + 1]
        elif sum_ < target:
            i += 1
        else:
            j -= 1
