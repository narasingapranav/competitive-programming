class Solution:
    def removeZeros(self, n: int) -> int:
        k=1
        s=0
        while n>0:
            rem=n%10
            if rem !=0:
                s+=rem*k
                k*=10
            n//=10
        return s