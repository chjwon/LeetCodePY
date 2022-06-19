from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sol = []
        if len(digits) == 0:
            return sol
        from itertools import product
        letter = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
                  '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
                  '8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits) == 1:
            return letter[digits]
        elif len(digits) == 2:
            for i in list(product(letter[digits[0]],letter[digits[1]])):
                sol.append("".join(list(i)))
            return sol
        elif len(digits) == 3:
            for i in list(
                product(letter[digits[0]],letter[digits[1]],
                        letter[digits[2]])):
                sol.append("".join(list(i)))
            return sol
        else:
            for i in list( product(letter[digits[0]],letter[digits[1]],
                                letter[digits[2]],letter[digits[3]])):
                sol.append("".join(list(i)))
            return sol
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sol = []
        if len(digits) == 0:
            return sol
        from itertools import product
        letter = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
                  '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
                  '8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits) == 1:
            return letter[digits]
        elif len(digits) == 2:
            for i in list(product(letter[digits[0]],letter[digits[1]])):
                sol.append("".join(list(i)))
            return sol
        elif len(digits) == 3:
            for i in list(
                product(letter[digits[0]],letter[digits[1]],
                        letter[digits[2]])):
                sol.append("".join(list(i)))
            return sol
        else:
            for i in list( product(letter[digits[0]],letter[digits[1]],
                                letter[digits[2]],letter[digits[3]])):
                sol.append("".join(list(i)))
            return sol
