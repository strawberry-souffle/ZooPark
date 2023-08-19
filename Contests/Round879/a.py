from collections import Counter
import math
t = int(input())
as_ = [0] * t
for i in range(t):
    input()
    as_[i] = [int(x) for x in input().split()]

for a in as_:
    elements: dict = Counter(a)
    toRemove = max(math.ceil((elements[-1] - elements[1])/2), 0)
    print(toRemove if (elements[-1] - toRemove) % 2 == 0 else toRemove + 1)