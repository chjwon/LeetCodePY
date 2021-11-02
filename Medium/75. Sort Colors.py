class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0 or 1:
            pass
        elif length == 2:
            if nums[0] > nums[1]:
                nums[0],nums[1] = nums[1],nums[0]
        else:
            val0 = nums.count(0)
            val1 = nums.count(1)
            val2 = length - val0 - val1
            for i in range(length):
                if i < val0:
                    nums[i] = 0
                elif i < val0+val1:
                    nums[i] = 1
                else:
                    nums[i] = 2
            print(nums)
            