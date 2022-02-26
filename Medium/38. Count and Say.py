class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev_sequence = self.countAndSay(n - 1)
            
            result_sequence = ""
            counter = {}
            for i in range(0, len(prev_sequence)):
                digit = prev_sequence[i]
                                
                if digit not in counter:
                    for key, value in counter.items():
                        result_sequence += str(value) + key                          
                    counter = {}
                    counter[digit] = 1
                                
                else:
                    counter[digit] += 1
            
            for key, value in counter.items():
                result_sequence += str(value) + key              
            
            return result_sequence