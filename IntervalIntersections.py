firstList = [[4,11]]
secondList = [[1,2],[8,11],[12,13],[14,15],[17,19]]
def intervalIntersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    ans = []
    i = j = 0

    while i < len(firstList) and j < len(secondList):
        # Let's check if firstList[i] intersects secondList[j].
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection
        lo = max(firstList[i][0], secondList[j][0])
        hi = min(firstList[i][1], secondList[j][1])
        if lo <= hi:
            ans.append([lo, hi])

        # Remove the interval with the smallest endpoint
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return ans
print(intervalIntersection(firstList, secondList))