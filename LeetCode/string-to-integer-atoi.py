class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = -1 if s[:1] == '-' else 1
        if s[:1] in '-+': s = s[1:]
        num = 0
        for c in s:
            if not c.isdigit(): break
            num = num * 10 + int(c)
        num *= sign
        return max(-2**31, min(num, 2**31 - 1))