class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol = ""
        if len(strs) == 0:
            return sol
        minLen = len(strs[0])
        for i in strs:
            minLen = min(minLen,len(i))
        for i in range(minLen):
            temp = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != temp:
                    return sol
            sol += temp
        return sol