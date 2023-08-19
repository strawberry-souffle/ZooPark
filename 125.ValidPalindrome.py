def isPalindrome(s: str) -> bool:
    letters = set('abcdefghijklmnopqrstuvwxyz0123456789')
    s = s.lower()
    arr = [i for i in s if i in letters]
    if len(arr) <= 0:
        return False
    for i in range(0, int(len(arr) / 2) + 1):
        if arr[i] != arr[-i - 1]:
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))