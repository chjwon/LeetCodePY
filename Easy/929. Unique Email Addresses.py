class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        for i in emails:
            midIndex = i.index("@")
            front = i[:midIndex]
            back = i[midIndex:]
            if front.count('+') > 0:
                plusIndex = front.index('+')
                front = front[:plusIndex]
            front = front.replace('.','')
            temp = front+back
            # print(temp)
            if temp not in result:
                result.append(temp)
        return len(result)