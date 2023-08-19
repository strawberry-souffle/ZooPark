from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def goodNodes(root: TreeNode) -> int:
    count = 0
    def DFS(node: TreeNode, maxNode: int):
        nonlocal count
        if not node:
            return
        if node.val >= maxNode:
            count += 1
            DFS(node.left, node.val)
            DFS(node.right, node.val)
        else:
            DFS(node.left, maxNode)
            DFS(node.right, maxNode)
    DFS(root, -100000)
    return count