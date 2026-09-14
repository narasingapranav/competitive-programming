from itertools import permutations
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        f=m=""
        for i in s:
            if i==y:
                f+=i
            else:
                m+=i
        return f+m