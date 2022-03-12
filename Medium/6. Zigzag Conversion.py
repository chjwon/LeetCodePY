class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        def convertIndex(currIndex, increase):
            if increase == True:
                return currIndex + 1
            else:
                return currIndex - 1

        result = []
        for _ in range(numRows):
            result.append([])
        currIndex = 0
        increase = True
        for i in s:
            result[currIndex].append(i)
            if currIndex == 0:
                increase = True
            elif currIndex == numRows - 1:
                increase = False
            else:
                pass
            currIndex = convertIndex(currIndex,increase)
        temp = []
        for t in result:
            temp = temp+t
        sol = ''.join(map(str,temp))
        return sol