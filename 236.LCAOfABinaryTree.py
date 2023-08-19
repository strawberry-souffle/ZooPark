from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def DFS(node: TreeNode):
        if not node:
            return None
        elif node == p or node == q:
            return node
        else:
            leftLCA, rightLCA = DFS(node.left), DFS(node.right)
            if leftLCA and rightLCA:
                return node
            elif leftLCA:
                return leftLCA
            elif rightLCA:
                return rightLCA
            return None
    return DFS(root)