class Solution:
    def maxArea(self, height: List[int]) -> int:
        from itertools import combinations
        comb = list(combinations(range(len(height)),2))
        max = 0
        if len(comb) == 1:
            return min(height[comb[0][0]],height[comb[0][1]])
        def Area(left,right,inputList):
            return abs(left-right) * min(inputList[left],inputList[right])
        for i in range(len(comb)):
            temp = Area(comb[i][0],comb[i][1],height)
            if temp > max:
                max = temp
        return max
# Time Limit Exceeded