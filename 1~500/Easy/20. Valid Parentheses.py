class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        brackets={
            '}':'{', ')':'(', ']':'['
            }
        for temp in s:
            if temp in brackets.values(): # ( { [
                stack.append(temp)
            else: # ) } ]
                if stack and brackets[temp] == stack[-1] :  
                    stack.pop()
                else: 
                    return False # when the bracket pair doesn't match
        
        if stack:
            return False # ex-> ([)]
        return True
