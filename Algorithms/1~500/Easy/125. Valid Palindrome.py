class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        inputStr = []
        for i in range(len(s)):
            if ord(s[i]) >= 65 and ord(s[i]) <= 90: # upper
                inputStr.append(s[i].lower())
            elif ord(s[i]) >= 97 and ord(s[i]) <= 122: # lower
                inputStr.append(s[i])
            elif ord(s[i]) >= 48 and ord(s[i]) <= 57: # integer
                inputStr.append(s[i])
        
        if inputStr == inputStr[::-1]:
            return True
        else:
            return False