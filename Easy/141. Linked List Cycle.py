# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            fast, slow = head.next, head
            while fast != slow:
                slow=slow.next
                fast=fast.next.next
            return True
        except:
            return False