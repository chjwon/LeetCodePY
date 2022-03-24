# Definition for singly-linked list.
# Testing the code for problem using LinkedList
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add(val):
    node = head
    while node.next: # check if node.next is null
        node = node.next # loop for next node
    node.next = ListNode(val) # new node

def addList(numList):
    for num in numList:
        add(num)

def printout(node):
    while node.next:
        print(node.val,end=' ')
        node = node.next
    print(node.val)

nodeTemp = ListNode(1)
head = nodeTemp
# add(2)
# add(3)
# add(4)
# add(5)
# printout(head) # 1,2,3,4,5
# temp = [6,7,8]
# addList(temp)
# printout(head)