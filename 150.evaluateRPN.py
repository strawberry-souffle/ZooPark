from collections import deque
def evalRPN(tokens: list[str]) -> int:
    q = deque()
    for t in tokens:
        if t == "+":
            q[-2] += q[-1]
            q.pop()
        elif t == "-":
            q[-2] -= q[-1]
            q.pop()
        elif t == "*":
            q[-2] *= q[-1]
            q.pop()
        elif t == "/":
            q[-2] = int(q[-2] / q[-1])
            q.pop()
        else:
            q.append(int(t))
    return q.pop()

print(evalRPN(["2","1","+","3","*"]))