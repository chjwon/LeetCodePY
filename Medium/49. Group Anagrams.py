class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            sol = {}
            for i in range(len(strs)):
                temp = "".join(sorted(strs[i]))
                if temp not in sol:
                    sol[temp] = [strs[i]]
                else:
                    sol[temp].append(strs[i])
            return sol.values()