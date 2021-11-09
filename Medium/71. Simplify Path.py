class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for temp in path.split('/'):
            temp = temp.replace('/','',temp.count('/'))
            if temp == '.' or temp == "":
                continue
            elif temp == "..":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(temp)
        return '/' + '/'.join(res)