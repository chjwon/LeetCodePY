class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        sol = 1
        for i in range(max(m,n)+1,m+n+1):
            sol *= i
        return sol // (math.factorial(min(m,n)))


"""
Runtime: 20 ms, faster than 99.45% of Python3 online submissions for Unique Paths.
Memory Usage: 14.4 MB, less than 39.12% of Python3 online submissions for Unique Paths.
"""