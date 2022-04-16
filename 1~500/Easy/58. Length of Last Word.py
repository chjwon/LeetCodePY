class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split(' ')
        word = [w for w in word if w != '']
        if len(word) == 0:
            return 0
        else:
            return len(word[-1])