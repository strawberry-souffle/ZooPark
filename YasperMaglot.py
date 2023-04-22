# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

arr = ListNode(1)
arr.next = ListNode(2)
arr.next.next = ListNode(3)
arr.next.next.next = ListNode(3)
arr.next.next.next.next = ListNode(4)
arr.next.next.next.next.next = ListNode(4)
arr.next.next.next.next.next.next = ListNode(5)
# arr.next.next.next.next.next.next.next = ListNode(4)
# arr.next.next.next.next.next.next.next.next = ListNode(4)
def deleteDuplicates(head: ListNode):
    sentinel = ListNode(0, head)

    # predecessor = the last node
    # before the sublist of duplicates
    pred = sentinel

    while head:
        # if it's a beginning of duplicates sublist
        # skip all duplicates
        if head.next and head.val == head.next.val:
            # move till the end of duplicates sublist
            while head.next and head.val == head.next.val:
                head = head.next
            # skip all duplicates
            pred.next = head.next
            # otherwise, move predecessor
        else:
            pred = pred.next

            # move forward
        head = head.next

    return sentinel.next
arr = deleteDuplicates(arr)
print(arr.val)
out = arr.next
while out:
    print(out.val)
    out = out.next