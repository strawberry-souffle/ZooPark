from collections import deque

class Node:
    def __init__(self, val: int = 0, left= None, right= None, next= None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(7)
def connect(root: Node) -> Node:
    def traverseLevel(head):
        curr = head.next
        head.next = None
        prev = head
        while curr:
            if curr.left:
                prev.next = curr.left
                prev = curr.left
            if curr.right:
                prev.next = curr.right
                prev = curr.right
            curr = curr.next
        if(head.next):
            traverseLevel(head)
    head = Node(-999)
    head.next = root
    traverseLevel(head)
    return root

connect(root)
