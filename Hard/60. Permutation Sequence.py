class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        originStr = ""
        for i in range(1,n+1):
            originStr += str(i)
        from itertools import permutations
        sol = ""
        for k in list(permutations(originStr,n))[k-1]:
            sol += k
        return sol
        