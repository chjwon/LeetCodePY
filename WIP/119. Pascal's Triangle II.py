#WIP
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def paskal(num):
            if num == 1:
                return [1]
            else:
                front = paskal(num - 1) + [0]
                back = [0] + paskal(num - 1)
                return [front[i] + back[i] for i in range(len(front))]
        return paskal(rowIndex+1)