# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # =====
        def compare(tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
            if tree1 is None and tree2 is None:
                return True
            elif tree1 is None or tree2 is None:
                return False
            elif tree1.val != tree2.val:
                return False
            else:
                return compare(tree1.left, tree2.left) and compare(tree1.right, tree2.right)
        # =====
        if compare(root, subRoot):
            return True
        if root.left is None:
            if root.right is None:
                return False
            else:
                return self.isSubtree(root.right,subRoot)
        else:
            if root.right is None:
                return self.isSubtree(root.left,subRoot)
            else:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)