import bisect


def minDistance(word1: str, word2: str) -> int:
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        letters = dict()
        for i in range(len(text2)):
            if text2[i] in letters:
                letters[text2[i]].append(i)
            else:
                letters[text2[i]] = [i]
        tails = [-1]
        for i in list(text1):
            if i not in letters:
                continue
            addingIndex = bisect.bisect_right(letters[i], tails[-1])
            if addingIndex < len(letters[i]):
                tails.append(letters[i][addingIndex])
            for l in reversed(range(0, addingIndex)):
                ind = bisect.bisect_left(tails, letters[i][l])
                # if ind < len(tails): actually not needed because of reversed()
                tails[ind] = letters[i][l]
        return len(tails) - 1
    return (len(word1) + len(word2)) - (2 * longestCommonSubsequence(word1, word2))

print(minDistance("leetcode", "etco"))