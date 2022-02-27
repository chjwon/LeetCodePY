class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        def detectPattern(word):
            alpha = {}
            sol = []
            num = 0
            for i in word:
                if i in alpha.keys():
                    sol.append(alpha[i])
                else:
                    alpha[i] = num
                    sol.append(alpha[i])
                    num+=1
            # print("For",word,sol)
            return sol

        pattern = detectPattern(pattern)
        sol = []
        for i in words:
            if pattern == detectPattern(i):
                # print(i)
                sol.append(i)
        return sol