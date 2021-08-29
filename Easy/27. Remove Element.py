class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        temp = 0
        sol=[]
        for i in range(length):
            if nums[i] == val:
                pass
            else:
                nums[temp]=nums[i]
                temp += 1
        return temp