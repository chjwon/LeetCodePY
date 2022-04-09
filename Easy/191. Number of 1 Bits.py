class Solution:
    def hammingWeight(self, n: int) -> int:
        n = "{0:b}".format(n)
        return str(n).count("1")