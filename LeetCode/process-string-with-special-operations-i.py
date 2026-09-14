class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        for i in s:
            if i.islower():
                res.append(i)
            elif i=='*':
                if res:
                    res.pop()
            elif i=='#':
                res+=res
            elif i=='%':
                res.reverse()
        return "".join(res)