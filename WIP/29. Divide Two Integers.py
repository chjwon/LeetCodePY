class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        temp = dividend // divisor
        sol = temp if temp >= 0 else temp +1
        return sol