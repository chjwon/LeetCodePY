class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        from itertools import combinations
        temp = [*range(1,n+1)]
        print(temp)
        for i in list(combinations(temp,k)):
            sol.append(list(i))
        return sol