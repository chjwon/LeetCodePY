class Solution:
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def fibo(n):
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                return fibo(n-1)+fibo(n-2)
        return fibo(n)