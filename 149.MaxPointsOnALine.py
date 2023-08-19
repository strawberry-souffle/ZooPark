def maxPoints(points: list[list[int]]) -> int:
    if len(points) <= 2:
        return len(points)
    output = 2
    for i in range(len(points) - 1):
        formedLines = dict()
        x = 0
        y = 0
        for j in range(i + 1, len(points)):
            x = (points[j][0] - points[i][0])
            if x < 0:
                x = -x
                y = (points[i][1] - points[j][1])
                vector = (1, y / x)
            elif x == 0:
                vector = (0, 1)
            else:
                y = (points[j][1] - points[i][1])
                vector = (1, y / x)
            if vector in formedLines:
                formedLines[vector] += 1
            else:
                formedLines[vector] = 2
        output = max(output, max(formedLines.values()))
    return output
print(maxPoints([[1,1],[2,2],[3,3]]))