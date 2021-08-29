class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        temp = prices[0]
        for i in range(1,len(prices)):
            tt = prices[i] - temp
            if tt > max:
                max = tt
            elif tt < 0:
                temp = prices[i]
        return max