def letterCombinations(digits: str) -> list[str]:
    if len(digits) <= 0:
        return []
    phone_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    output: list[str] = []
    def dfs(path, depth):
        if depth == len(digits):
            output.append(path)
            return
        for l in phone_map[digits[depth]]:
            dfs(path + l, depth + 1)

    dfs("", 0)
    return output

print(letterCombinations("23"))