from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sol=[]
        for i in range(len(nums)):
            sol.append(sum(nums[:i+1]))
        return sol

        """
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
        """