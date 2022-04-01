from typing import List


class BinarySearchTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = 1

    def add(self, num : int):
        if self.val:
            if num < self.val:
                if self.left is None:
                    self.left = BinarySearchTree(num)
                else:
                    self.left.add(num)
            elif num > self.val:
                if self.right is None:
                    self.right = BinarySearchTree(num) 
                else:
                    self.right.add(num)
            else: # same
                self.count += 1

        else:
            self.val = num

    def addList(self, numList: List[int]):
        for num in numList:
            if type(num) is int:
                self.add(num)

    def printDescending(self):
        if self.left:
            self.left.printDescending()
        print(self.val)
        if self.right:
            self.right.printDescending()

print("test")
temp = BinarySearchTree(5)
tt = [3,6,2,4,None,None,1]
temp.addList(tt)
temp.printDescending()