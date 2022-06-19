from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for _ in range(k-1):
            nums.remove(max(nums))
        return max(nums)