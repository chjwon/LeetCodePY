from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = words[0]
        sol=[]
        for alpha in temp:
            flag = True
            for i in range(1,len(words)):
                if not alpha in words[i]:
                    flag = False
                if alpha in words[i]:
                    if sol.count(alpha) >= words[i].count(alpha):
                        flag = False
            if flag:
                sol.append(alpha)
        return sol