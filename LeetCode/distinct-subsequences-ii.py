class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        last = {}
        for ch in s:
            old = dp
            dp = 2 * dp - last.get(ch, 0)
            last[ch] = old
            dp %= MOD
        return (dp - 1)%MOD