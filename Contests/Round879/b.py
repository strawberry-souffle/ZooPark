import math
def standartSolution(l, r):
    answer = (len(l) - 1) * 9
    if len(l) > len(r):
        answer += int(l[0])
    else:
        answer += int(math.fabs(int(l[0]) - int(r[0])))
    return answer
t = int(input())
a = [0] * t
for i in range(t):
    a[i] = [str(x) for x in input().split()]
for a_ in a:
    l, r = a_[0], a_[1]
    if len(r) > len(l):
        l, r = r, l
    answer = 0
    if len(l) > len(r) or int(math.fabs(int(l[0]) - int(r[0]))) > 0:
        answer = standartSolution(l, r)
    else:
        for j in range(len(l)):
            if l[j] != r[j]:
                answer = standartSolution(l[j:], r[j:])
                break
    print(answer)
