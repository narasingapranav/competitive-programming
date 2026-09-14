class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9 +7
        ep=(n+1) >>1
        op=n>>1 
        return (pow(4,op,MOD)*pow(5,ep,MOD))% MOD