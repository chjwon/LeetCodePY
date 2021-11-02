class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        x = 0
        for i in operations:
            if i[1] == '+':
                x += 1
            elif i[1] == "-":
                x -= 1
        return x
        """
        x = 0
        for i in operations:
            x = eval(str(x)+i[1]+"1")
        return x
    