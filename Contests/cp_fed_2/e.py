import math
def findBestDivisor(s):
    for i in reversed(range(1, int(math.sqrt(s)) + 1)):
        if s % i ==0:
            return i

s = int(input())
a = findBestDivisor(s)
print(((max(int(s/a), a))**2) - s)