class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        from itertools import combinations
        comb = list(combinations(nums,3))
        diff=[]
        for i in comb:
            diff.append(abs(sum(i)-target))
        return sum(comb[diff.index(min(diff))])
# Time Limit Exceeded