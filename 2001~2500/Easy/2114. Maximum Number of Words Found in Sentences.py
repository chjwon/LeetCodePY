from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sol = 0
        for i in sentences:
            sol = max(sol,i.count(' ')+1)
        return sol