class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        if 1000<=n<=100000:
            return 1+n-1000