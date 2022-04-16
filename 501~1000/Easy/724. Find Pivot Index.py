from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums)):
            left = sum(nums[:i])
            if left * 2 == total - nums[i]:
                return i
        return -1
            