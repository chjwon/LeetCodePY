class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def eFunc(num):
            return num//2
        def oFunc(num):
            return 3*num+1
        
        def powerVal(num):
            sol = 0
            while num != 1:
                if num % 2 == 0:
                    num = eFunc(num)
                else:
                    num = oFunc(num)
                sol += 1
            return sol
        
        solNum = {}
        for i in range(lo,hi+1):
            solNum[i] = powerVal(i)
        solNum = sorted(solNum.items(), key=lambda x: x[1])
        return solNum[k-1][0]