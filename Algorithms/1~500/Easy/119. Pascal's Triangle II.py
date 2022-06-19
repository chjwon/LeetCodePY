class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        solList = [[1],[1,1]]
        if rowIndex == 0 or rowIndex == 1:
            return solList[rowIndex]
        else:
            for i in range(1, rowIndex): # (1,3) -> 1,2
                temp = [1]
                for j in range(len(solList[i])-1):
                    temp.append(solList[i][j]+solList[i][j+1])
                temp.append(1)
                solList.append(temp)
            return solList[rowIndex]