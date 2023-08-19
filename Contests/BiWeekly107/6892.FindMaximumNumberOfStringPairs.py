def maximumNumberOfStringPairs(words: list[str]) -> int:
    reversed_arr = [i[::-1] for i in words]
    output = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == reversed_arr[j]:
                output += 1
    return output
print(maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))