import math
n, m = map(int, input().split())
c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
minHour = d[0]
if m % c[0] == 0:
    maxHour = minHour + ((m // c[0]) - 1)
else:
    maxHour = minHour + (m // c[0])
minPortion = min(c[0], m)
for i in range(1, len(c)):
    if c[i] >= minPortion:
        minHour += d[i]
        maxHour += d[i]
    else:
        minHour += d[i]
        # maxHour = minHour + (math.ceil(m / c[i]) - 1)
        if m % c[i] == 0:
            maxHour = minHour + ((m // c[i]) - 1)
        else:
            maxHour = minHour + (m // c[i])
        minPortion = c[i]

print(maxHour)