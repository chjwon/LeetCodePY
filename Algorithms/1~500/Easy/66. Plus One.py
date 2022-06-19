class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        num = 0
        for i in range(length):
            num += (10**(length-i-1)) * digits[i]
        num += 1
        length = len(str(num))
        sol = []
        for i in range(length):
            sol.append(str(num)[i])
        return sol