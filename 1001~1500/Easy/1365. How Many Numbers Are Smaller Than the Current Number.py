from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sol = []
        for i in nums:
            temp = 0
            for j in nums:
                if i > j:
                    temp += 1
            sol.append(temp)
        
        return sol