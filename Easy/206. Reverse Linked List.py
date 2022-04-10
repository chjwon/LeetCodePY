# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        temp = ListNode(head.val)
        while head.next:
            head = head.next
            cur = ListNode(head.val)
            cur.next = temp
            temp = cur
        return temp