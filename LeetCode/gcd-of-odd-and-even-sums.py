class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        es=sum(i for i in range(2,2*n,2))
        os=sum(i for i in range(1,2*n,2))
        return gcd(os,es)