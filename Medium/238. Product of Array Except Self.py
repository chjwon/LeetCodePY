class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = []
        length = len(nums)
        for i in nums:
            if i == 0:
                if len(zero) == 0:
                    zero.append(nums.index(i))
                else:
                    return [0]*length
            else:
                total *= i
        if len(zero) == 0:
            sol = []
            for i in nums:
                sol.append(total//i)
            return sol
        else:
            sol = [0]*length
            sol[zero[0]] = total
            return sol