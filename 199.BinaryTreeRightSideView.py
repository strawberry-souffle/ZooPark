from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def rightSideView(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    q = deque([root])
    answer = list()
    dummy = TreeNode(val=-69)
    newLevelHead = root
    while q:
        node = q.popleft()
        if node == newLevelHead:
            answer.append(node.val)
            if node.right:
                newLevelHead = node.right
            elif node.left:
                newLevelHead = node.left
            else:
                newLevelHead = dummy
        elif newLevelHead == dummy:
            if node.right:
                newLevelHead = node.right
            elif node.left:
                newLevelHead = node.left
            else:
                newLevelHead = dummy
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return answer