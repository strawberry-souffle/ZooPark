s = "cbaebabacd"
p = "abc"
def findAnagrams(s: str, p: str) -> list[int]:
    win_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    p_len = len(p)
    s_len = len(s)
    if p_len > s_len:
        return None
    keys = set(p)
    out = []
    for i in p:
        win_dict[i] += 1
    l = 0
    for i in range(l, p_len):
        win_dict[s[i]] -= 1
    Add = True
    for i in keys:
        if win_dict[i] > 0:
            Add = False
    if Add:
        out.append(l)
    while l < s_len - p_len:
        l += 1
        win_dict[s[l - 1]] += 1
        win_dict[s[l + p_len - 1]] -= 1
        Add = True
        for i in keys:
            if win_dict[i] > 0:
                Add = False
        if Add:
            out.append(l)
    return out
print(findAnagrams(s, p))