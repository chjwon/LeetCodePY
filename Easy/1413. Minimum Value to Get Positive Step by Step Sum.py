class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sumList = []
        for i in range(len(nums)):
            sumList.append(sum(nums[:i+1]))
        minNum = min(sumList)
        print(sumList)
        if minNum < 0:
            return -minNum + 1
        else:
            return 1