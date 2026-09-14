class Solution:
    def romanToInt(self, s: str) -> int:
        d={
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        total=0
        pre=0
        for i in reversed(s):
            n=d[i]
            if n<pre:
                total-=n
            else:
                total+=n
                pre=n
        return total