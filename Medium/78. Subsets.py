class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        sol = [(),]
        for i in range(1,len(nums)+1):
            temp = combinations(nums,i)
            sol.extend(temp)
            print(sol)
        for i in range(len(sol)):
            sol[i] = list(sol[i])
                              
        return sol