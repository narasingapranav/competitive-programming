from itertools import permutations
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        f=m=l=""
        for i in s:
            if i==y:
                f+=i
            elif i==x:
                l+=i
            else:
                m+=i
        return f+m+l