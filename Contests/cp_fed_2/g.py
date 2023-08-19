_, m = map(int, input().split())
a = [int(i) for i in input().split()]
queries = [input().split() for _ in range(m)]
for q in queries:
    l, r = map(int, q)
    l, r = l-1, r-1
    count = r - l + 2
    subStart = l
    for i in range(l + 1, r + 1):
        if a[i] != a[i - 1]:
            count -= (i - subStart + 1) - 2
            subStart = i
    count -= ((r + 1) - subStart + 1) - 2
    print(count)