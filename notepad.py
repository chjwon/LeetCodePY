def maxArea(self, height) -> int:
    def Area(left,right,inputList):
        return abs(left-right) * min(inputList[left],inputList[right])
    from itertools import combinations
    comb = list(combinations(height,2))
    print(comb)
    max = 0
    for i in range(len(comb)):
        temp = Area(comb[i][0],comb[i][1],height)
        print(temp)
        if temp > max:
            max = temp
    return max
ii = [1,1]
print(maxArea(1,ii))