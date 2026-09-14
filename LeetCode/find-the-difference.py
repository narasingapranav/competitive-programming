class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        for i in s:
            if i in t:
                t.remove(i)
        return t[0]