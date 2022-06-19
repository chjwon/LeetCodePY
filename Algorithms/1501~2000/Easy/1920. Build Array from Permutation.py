from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        sol = []
        for i in nums:
            sol.append(nums[i])
        return sol

        """
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
        """