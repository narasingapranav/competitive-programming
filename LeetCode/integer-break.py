class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        if n==3: return 2
        q=n//3
        r=n%3
        return 3**q if r==0 else 3**(q-1) * 4 if r==1 else (3**q) * 2
