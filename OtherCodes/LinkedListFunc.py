# Definition for singly-linked list.
# Testing the code for problem using LinkedList
from typing import List


class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, num : int):
        while self.next: # check if node.next is null
            self = self.next # loop for next node
        self.next = LinkedList(num) # new node

    def addList(self, numList : List[int]):
        for num in numList:
            self.add(num)

    def printout(self):
        while self.next:
            print(self.val,end=' ')
            self = self.next
        print(self.val)

nodeTemp = LinkedList(1)
nodeTemp.add(2)
nodeTemp.printout() # 1,2
temp = [6,7,8]
nodeTemp.addList(temp)
nodeTemp.printout() # 1,2,6,7,8