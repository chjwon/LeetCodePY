from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        maxPos = 0
        end = 0
        steps = 0
        for i in range(len(nums)-1):
            maxPos = max(maxPos,i+nums[i])
            if i == end:
                end = maxPos
                steps += 1
                
        return steps
