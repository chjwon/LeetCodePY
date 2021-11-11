class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        temp = [0]*len(nums)
        temp[0] = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            temp[i] = max(temp[i-1]+nums[i], nums[i])
            if temp[i]>max_num: max_num = temp[i]
        return max_num