class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        sol=[[1]]
        for _ in range(2,numRows+1):
            paskal = [(sol[-1] + [0])[i] + ([0] + sol[-1])[i] for i in range(len(sol[-1]+[0]))]
            sol.append(paskal)
        return sol