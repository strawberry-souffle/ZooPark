from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def DFS(node: TreeNode):
        if not node:
            return (-1, -1)#diameter, height
        leftProperties = DFS(node.left)
        rightProperties = DFS(node.right)
        return (max(max(leftProperties[0], rightProperties[0]), leftProperties[1] + rightProperties[1] + 2),
                max(leftProperties[1], rightProperties[1]) + 1)

    return max(DFS(root))

def diameterOfBinaryTree_NoRedundancy(root: Optional[TreeNode]) -> int:
    answer = 0
    def DFS(node: TreeNode):
        if not node:
            return -1
        leftH = DFS(node.left)
        rightH= DFS(node.right)
        nonlocal answer
        answer = max(answer, leftH + rightH + 2)
        return max(leftH, rightH) + 1

    DFS(root)
    return answer