class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        c=0
        while n>1:
            if (n&1) and ((n>>1)&1):
                c+=1
            n>>=1
        return c==1