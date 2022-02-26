class Solution:
    def isHappy(self, n: int) -> bool:
        def loopNum(n:int):
            sol = 0
            for i in range(len(str(n))):
                sol += int(str(n)[i])**2
            return sol
        sol = False
        flag = True
        happy = [n]
        temp = n
        while flag:
            temp = loopNum(temp)
            if temp == 1 or temp%10 == 0:
                flag = False
                sol = True
                return sol
            elif temp in happy:
                flag = False
                return sol
            else:
                happy.append(temp)
