def longestPalindrome(s: str) -> str:
    bestPalindrome = ""
    s_len = len(s)
    def Palindrome(i, j):
        if i >= 0 and j < s_len and s[i] == s[j]:
            return Palindrome(i - 1, j + 1)
        else:
            return tuple((i + 1, j - 1))
    for i in range(0, s_len):
        palindrome1 = Palindrome(i, i)
        palindrome2 = Palindrome(i, i + 1)
        p2_len = palindrome2[1] - palindrome2[0] + 1
        p1_len = palindrome1[1] - palindrome1[0] + 1
        if p2_len > p1_len:
            if p2_len > len(bestPalindrome):
                bestPalindrome = s[palindrome2[0]:palindrome2[1] + 1]
        else:
            if p1_len > len(bestPalindrome):
                bestPalindrome = s[palindrome1[0]:palindrome1[1] + 1]

    return bestPalindrome

print(longestPalindrome("iptmykvjanwiihepqhzupneckpzomgvzmyoybzfynybpfybngttozprjbupciuinpzryritfmyxyppxigitnemanreexcpwscvcwddnfjswgprabdggbgcillisyoskdodzlpbltefiz"))
