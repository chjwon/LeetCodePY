# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            sol = head = ListNode(list1.val)
            list1 = list1.next
        else:
            sol = head = ListNode(list2.val)
            list2 = list2.next

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                sol.next = ListNode(list1.val)
                list1 = list1.next
            else:
                sol.next = ListNode(list2.val)
                list2 = list2.next
            sol = sol.next
        while list1 is not None:
            sol.next = ListNode(list1.val)
            list1 = list1.next
            sol = sol.next
        while list2 is not None:
            sol.next = ListNode(list2.val)
            list2 = list2.next
            sol = sol.next
        
        return head
        