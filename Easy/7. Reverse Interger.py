class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minus = False
        if x<0:
            minus = True
            sol = str(-x)
        else:
            sol = str(x)
        sol = sol[::-1]
        
        sol = int(sol)
        if minus:
            sol = -sol
        if sol >= 2**31-1 or sol <= -2**31:
            return 0
        else:
            return sol