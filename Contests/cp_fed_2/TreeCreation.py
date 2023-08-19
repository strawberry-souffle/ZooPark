from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []
        self.path = list()

Nodes = [TreeNode(i) for i in range(int(input()))]
connections = [0] * int(input())
for i in range(len(connections)):
    connections[i] = tuple(map(int, input().split()))
root = Nodes[0]
root.path = [root]
for i in connections:
    Nodes[i[0]].children.append(Nodes[i[1]])
    Nodes[i[1]].path = Nodes[i[0]].path.copy() + [Nodes[i[1]]]

print("Tree Created")

def findLCA(p: TreeNode, q: TreeNode):
    maxD = min(len(p.path), len(q.path))
    for i in range(0, maxD):
        if p.path[i] != q.path[i]:
            return p.path[i - 1]
    return p.path[maxD - 1]

i, j = map(int, input().split())
LCA = findLCA(Nodes[i], Nodes[j])
print(LCA)
