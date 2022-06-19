class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            temp = s[0:i]+s[i+1:]
            if s[i] not in temp:
                return i
            
        return -1
            