from collections import deque


def wordBreak(s: str, wordDict: list[str]) -> bool:
    memo = [-1] * len(s)
    wordSet = set(wordDict)

    def wordBreakMemo(start: int):
        if start == len(s):
            return True
        if memo[start] != -1:
            return memo[start]
        else:
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and wordBreakMemo(end):
                    memo[start] = True
                    return memo[start]
            memo[start] = False
            return memo[start]

    return wordBreakMemo(0)

# Idk previous one is better
def wordBreak_DP(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # empty string can be segmented into an empty sequence of words

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]  # return the final answer

#Witty enough, but isn't really worth it
def wordBreak_BFS(s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)
    q = deque()
    len_s = len(s)
    q.append(0)
    visited = set()
    while q:
        start = q.popleft()
        if start in visited:
            continue
        for i in range(start + 1, len_s + 1):
            if s[start:i] in wordSet:
                q.append(i)
                if i >= len_s:
                    return True
        visited.add(start)
    return False

print(wordBreak_BFS("leetcode", ["leet","code"]))

