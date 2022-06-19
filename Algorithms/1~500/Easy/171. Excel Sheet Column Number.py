class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 26
        ordNum = 64
        temp = columnTitle[::-1]
        sol = 0
        for i in range(len(temp)):
            sol += (ord(temp[i])-ordNum) * (num**(i))
        return sol