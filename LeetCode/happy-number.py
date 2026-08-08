class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            su = 0
            for i in str(n):
                su += int(i) ** 2
            n = su
        return n == 1