height = [1,8,6,2,5,4,8,3,7]
def maxArea(height: list[int]) -> int:
    i = 0
    j = len(height) - 1
    maxArea = 0
    while i != j:
        area = (j - i) * min(height[i], height[j])
        if area > maxArea:
            maxArea = area
        if height[i] < height[j]:
            i += 1
        else:
            j += -1
    return maxArea
print(maxArea(height))