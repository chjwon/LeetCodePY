class Solution:
    def minDominoRotations(self, tops, bottoms) -> int:
        def search(integrateArray, keyNum):
            solTop = 0
            solBottom = 0
            result = True
            for i in integrateArray:
                # print("=====")
                if keyNum in i:
                    if i[0] == i[1]:
                        pass
                    else:
                        # print("KeyNum",keyNum, "in",i,"Add top : ",i.index(keyNum)," Add Bottom : ",(i.index(keyNum)+1)%2)
                        solTop += i.index(keyNum)
                        solBottom += (i.index(keyNum)+1)%2
                else:
                    return False, -1, -1
            return True, solTop, solBottom
            
        solTop = 0
        solBottom = 0
        fail = -1
        arraySize = len(tops)
        integrate = []
        keyNumArr = []
        for i in range(arraySize):
            integrate.append([tops[i],bottoms[i]])
        if integrate[0][0] in integrate[1]:
            keyNumArr.append(integrate[0][0])
        if integrate[0][1] in integrate[1]:
            keyNumArr.append(integrate[0][1])
        if len(keyNumArr) == 0:
            return fail
        flag = True
        for keyNum in keyNumArr:
            flag, solTop, solBottom = search(integrate, keyNum)
            if flag == True:
                # print("keyNum : ", keyNum)
                # print("top : ",solTop)
                # print("Bottom : ",solBottom)
                return min(solTop,solBottom)
            else:
                pass
        if flag == False:
            return fail