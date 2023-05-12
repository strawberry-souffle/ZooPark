s: str = (input())
k = 0
letter_to_number = {
        'a': -1,
        'b': -1,
        'c': -1,
        'd': -1,
        'e': -1,
        'f': -1,
        'g': -1,
        'h': -1,
        'i': -1,
        'j': -1,
        'k': -1,
        'l': -1,
        'm': -1,
        'n': -1,
        'o': -1,
        'p': -1,
        'q': -1,
        'r': -1,
        's': -1,
        't': -1,
        'u': -1,
        'v': -1,
        'w': -1,
        'x': -1,
        'y': -1,
        'z': -1,
        '0': -1,
        '1': -1,
        '2': -1,
        '3': -1,
        '4': -1,
        '5': -1,
        '6': -1,
        '7': -1,
        '8': -1,
        '9': -1,
        ' ': -1,
        '!': -1,
        '@': -1,
        '#': -1,
        '$': -1,
        '%': -1,
        '&': -1,
        '*': -1,
        '(': -1,
        ')': -1,
        '-': -1,
        '_': -1,
        '+': -1,
        '=': -1,
        '[': -1,
        ']': -1,
        '{': -1,
        '}': -1,
        ';': -1,
        ':': -1,
        ',': -1,
        '.': -1,
        '<': -1,
        '>': -1,
        '/': -1,
        '?': -1,
        '|': -1,
        '`': -1,
        '~': -1
    }
longestStr = ""
for i in range(0, len(s)):
    if letter_to_number[s[i]] == -1:
        letter_to_number[s[i]] = i
    else:
        if len(s[k:i]) > len(longestStr):
            longestStr = s[k:i]
        for j in range(k, letter_to_number[s[i]]):
            letter_to_number[s[j]] = -1
        k = letter_to_number[s[i]] + 1
        letter_to_number[s[i]] = i
if len(s[k:]) > len(longestStr):
    longestStr = s[k:]
print(len(longestStr))

import random
grid = [[random.randint(0,1) for _ in range(20)] for _ in range(20)]
print(grid)