class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list=[]
        for item in nums:
            if item in list:
                list.remove(item)
            else:
                list.append(item)
        return list[0]