from collections import deque
def isValid(s: str) -> bool:
    q = deque()
    for i in s:
        if i == '(' or i == '{' or i == '[':
            q.append(i)
        elif q:
            parent = q.pop()
            if not ((parent == '(' and i == ')') or (parent == '{' and i == '}') or (parent == '[' and i == ']')):
                return False
        else:
            return False
    return not q

print(isValid("(]"))