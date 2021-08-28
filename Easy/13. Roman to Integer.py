class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numDic = {
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        numList = []
        for i in range(len(s)):
            numList.append(numDic[s[i]])
        for i in range(len(numList)-1):
            if numList[i] < numList[i+1]:
                numList[i] = -numList[i]
        return sum(numList)