matrix: list[list[int]] = [[1,1]]
target = 2
def ElementFromMatrix(matrix, i):
    return matrix[i // len(matrix[0])][i % len(matrix[0])]
def binarySearchMatrix(matrix, k):
    def binaryRec(l, r):
        if(l > r):
            return -1
        m = (l + r) // 2
        if k == ElementFromMatrix(matrix, m):
            return m
        if k < ElementFromMatrix(matrix, m):
            return binaryRec(l, m - 1)
        else:
            return binaryRec(m + 1, r)
    ans = binaryRec(0, len(matrix) * len(matrix[0]) - 1)
    return ans
print(binarySearchMatrix(matrix, target))