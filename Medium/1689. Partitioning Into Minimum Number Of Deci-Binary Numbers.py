class Solution:
    def minPartitions(self, n: str) -> int:
        for i in range(10):
            temp = str(9-i)
            if temp in n:
                return temp