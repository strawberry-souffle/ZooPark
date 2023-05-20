def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0
    if len(s) <= 1:
        return 1
    def addElement(index, previousFree, output):
        if index >= len(s):
            return output

        if 1 <= int(s[index]) <= 2:
            return addElement(index + 1, output, output + previousFree)
        elif s[index] == '0':
            if previousFree > 0:
                return addElement(index + 1, 0, previousFree)
            else:
                return 0
        else:
            if int(s[index - 1]) == 1 or int(s[index]) <= 6:
                return addElement(index + 1, 0, output + previousFree)
            else:
                return addElement(index + 1, 0, output)
    return addElement(0, 0, 1)

print(numDecodings("230"))

