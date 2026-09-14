class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9 +7
        ep=(n+1) //2
        op=n//2 
        return (pow(4,op,MOD)*pow(5,ep,MOD))% MOD