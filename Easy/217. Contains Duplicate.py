from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                return True
        return False