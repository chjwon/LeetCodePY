class Solution:
    def search(self, nums, target: int) -> int:
        if target not in nums:
            return -1
        else:
            if target == nums[0]:
                return 0
            cut = nums.index(max(nums))
            temp1 = nums[:cut+1]
            temp2 = nums[cut+1:]
            if target > temp1[0]:
                return temp1.index(target)
            else:
                return temp2.index(target) + cut + 1