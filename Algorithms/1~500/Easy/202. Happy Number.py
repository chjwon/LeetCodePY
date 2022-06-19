class Solution:
    def isHappy(self, n: int) -> bool:
        
        def convertNum(n:int):
            sol = 0
            n = str(n)
            for i in n:
                sol += int(i)**2
            return sol
        
        isLoop = []
        flag = True
        while flag:
            if n in isLoop:
                flag = False
                return False
            else:
                isLoop.append(n)
            if n == 1:
                flag = False
                return True
            n = convertNum(n)