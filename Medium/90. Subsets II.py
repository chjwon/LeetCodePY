class Solution:
    def subsetsWithDup(self, nums):
        from itertools import combinations
        sol = [[]]
        for i in range(1,len(nums)+1):
            for ele in list(combinations(nums,i)):
                temp = list(ele)
                temp.sort()
                if temp not in sol:
                    sol.append(temp)
        return sol