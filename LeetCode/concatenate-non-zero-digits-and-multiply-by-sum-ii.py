from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries):
        MOD = 10**9 + 7

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        m = len(digits)

        pref = [0]*(m+1)
        value = [0]*(m+1)
        pow10 = [1]*(m+1)

        for i in range(m):
            pref[i+1] = pref[i] + digits[i]
            value[i+1] = (value[i]*10 + digits[i]) % MOD
            pow10[i+1] = (pow10[i]*10) % MOD

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r)

            if L == R:
                ans.append(0)
                continue

            digit_sum = pref[R] - pref[L]

            num = (value[R] - value[L] * pow10[R-L]) % MOD

            ans.append((num * digit_sum) % MOD)

        return ans