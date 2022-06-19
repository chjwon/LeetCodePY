class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        solList = []
        def checkIn(solList: List[List[int]], node):
            for i in solList:
                for j in i:
                    if j == node:
                        return True
            return False
        
        def connectTwo(solList: List[List[int]], node1, node2):
            for i in range(len(solList)):
                if node1 in solList[i]:
                    index1 = i
                if node2 in solList[i]:
                    index2 = i
            if index1 == index2:
                return solList
            else:
                temp1 = solList[index1]
                temp2 = solList[index2]
                solList.remove(temp1)
                solList.remove(temp2)
                solList.append(temp1+temp2)
                return solList
        
        
        for startNodeNum in range(len(isConnected)):
            # current node is startNodeNum + 1
            if checkIn(solList, startNodeNum) == False:
                    solList.append([startNodeNum])
            for targetNodeNum in range(len(isConnected[startNodeNum])):
                if checkIn(solList, targetNodeNum) == False:
                    solList.append([targetNodeNum])
                if isConnected[startNodeNum][targetNodeNum] == 1:
                    solList = connectTwo(solList, startNodeNum, targetNodeNum)
                else: # 0
                    pass
        return len(solList)