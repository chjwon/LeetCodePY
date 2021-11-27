class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        sol = []
        splitList = []
        for t in transactions:
            temp = t.split(',')
            temp[1] = int(temp[1])
            temp[2] = int(temp[2])
            splitList.append(temp)
        for unit in splitList:
            if unit[2] > 1000:
                unit[1] = str(unit[1])
                unit[2] = str(unit[2])
                sol.append(','.join(unit))
                continue
            for x in splitList:
                if unit[0] == x[0] and abs(unit[1]-int(x[1])) <= 60 and unit[3] != x[3]:
                    unit[1] = str(unit[1])
                    unit[2] = str(unit[2])
                    sol.append(','.join(unit))
                    break
        return sol
        