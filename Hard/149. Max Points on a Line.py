class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getFunction(Flist, Slist):
            # y = ax+b
            a=0
            b=0
            if Slist[0] - Flist[0] == 0:
                pass
            else:
                a = (Slist[1] - Flist[1]) / (Slist[0] - Flist[0])
                b = Flist[1] - (a * Flist[0])
            return (a,b) # it must be tuple to hash
        from itertools import combinations
        temp = list(combinations(points,2))
        for i in range(len(temp)):
            temp[i] = getFunction(temp[i][0],temp[i][1])
        # print("all lines: ",temp)
        lineCount = list(set(temp))
        # print("lineCount:  ",lineCount)
        for k in range(len(lineCount)):
            lineCount[k] = temp.count(lineCount[k])
        lineCount = list(set(lineCount))
        # print("lines : ",lineCount)
        if len(lineCount) == 0:
            return 1
        sol = max(lineCount)
        print("max line ",sol)
        def comb(n):
            return n * (n-1) // 2
        flag = True
        tt = 1
        if sol == 1:
            return 2
        elif sol == 3:
            return 3
        elif sol == 6:
            return 4
        while flag:
            if comb(tt) >= sol:
                flag = False
                return tt
                # print("sol : ",tt-1)
            else:
                tt += 1
        