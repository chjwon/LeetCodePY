class Solution:
    def getSum(self, a: int, b: int) -> int:
        list = []
        if a>=0 and b>=0:
            for _ in range(a):
                list.append(1)
            for _ in range(b):
                list.append(1)
            return len(list)
        elif (a>=0 and b<0):
            if a > abs(b):
                for _ in range(a):
                    list.append(1)
                for _ in range(abs(b)):
                    list.remove(1)
                return len(list)
            elif a < abs(b):
                for _ in range(abs(b)):
                    list.append(1)
                for _ in range(a):
                    list.remove(1)
                return -len(list)
            else:
                return 0
        
        elif (a<0 and b>=0):
            if abs(a) > b:
                for _ in range(abs(a)):
                    list.append(1)
                for _ in range(b):
                    list.remove(1)
                return -len(list)
            elif abs(a) < b:
                for _ in range(b):
                    list.append(1)
                for _ in range(abs(a)):
                    list.remove(1)
                return len(list)
            else:
                return 0
            
            
        else: # a<0 b<0
            for _ in range(abs(a)):
                list.append(1)
            for _ in range(abs(b)):
                list.append(1)
            return -len(list)
        
            