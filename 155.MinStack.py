from collections import deque
import math
# I'm genius. It works only because its a stack and not a deque, so this approach would shatter once you try to popleft elements.
class MinStack:

    def __init__(self):
        self.q = deque()
        self.minQ = deque([math.inf])#dummy head

    def push(self, val: int) -> None:
        self.q.append(val)
        if val <= self.minQ[-1]:# You can do that because updating greater elements is not correct, as the val will be popped earlier than anything else
            self.minQ.append(val)

    def pop(self) -> None:
        if self.q.pop() == self.minQ[-1]:
            self.minQ.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.minQ[-1]