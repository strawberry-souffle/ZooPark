from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    q = deque([root])
    answer = list()
    dummy = TreeNode(val=-69)
    newLevelHead = dummy
    currentLevelTraversal = list()
    while q:
        node = q.popleft()
        if node == newLevelHead:
            answer.append(currentLevelTraversal)
            currentLevelTraversal = []
            if node.left:
                newLevelHead = node.left
            elif node.right:
                newLevelHead = node.right
            else:
                newLevelHead = dummy
        elif newLevelHead == dummy:
            if node.left:
                newLevelHead = node.left
            elif node.right:
                newLevelHead = node.right
            else:
                newLevelHead = dummy
        currentLevelTraversal.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return answer + [currentLevelTraversal]