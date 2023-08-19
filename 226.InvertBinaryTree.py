from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def DFS(node: TreeNode):
        if not node:
            return None
        else:
            node.right, node.left = DFS(node.left), DFS(node.right)
            return node
    return DFS(root) if root else None