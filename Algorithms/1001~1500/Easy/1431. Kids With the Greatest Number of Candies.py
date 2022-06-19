class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sol = []
        maxNum = max(candies)
        for curr in candies:
            # print(curr+extraCandies)
            if curr + extraCandies >= maxNum:
                sol.append(True)
            else:
                sol.append(False)
        return sol