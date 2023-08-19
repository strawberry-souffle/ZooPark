import bisect
def isPalindrome(s: str) -> bool:
    if len(s) <= 0:
        return False
    for i in range(0, int(len(s) / 2) + 1):
        if s[i] != s[-i - 1]:
            return False
    return True
def binSearch(list_, finding):
    ind = bisect.bisect_left(list_,finding)
    return ind if list_[ind] == finding else -1
def find_indices(list_, item_to_find):
    indices = []
    for idx, value in enumerate(list_):
        if value == item_to_find:
            indices.append(idx)
    return indices
s = str(input())
Astart = find_indices(s, str(s[0]))
count = 0
for i_ in reversed(range(2, len(Astart))):
    i = Astart[i_]
    aLen = (len(s)-i)
    a = s[:aLen]
    if a == s[i:]:
        allowedRange = range(1, i_)
        for j_ in allowedRange:
            j = Astart[j_]
            if j > aLen and j + aLen < i and s[j:j + aLen] == a:
                n = s[j + aLen:i]
                if n == a:
                    continue
                st = s[aLen:j]
                count += max((len(st) - 1) - (1 if n == st[:len(n)] else 0) - (1 if n == st[len(st) - len(n):] else 0) - (1 if len(st) % 2 == 0 and st[:int(len(st)/2)] == st[int(len(st)/2):] else 0) - (1 if a == st[:aLen] else 0) - (1 if a == st[len(st) - aLen:] else 0), 0)
print(count)

