class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def p(n):
            ans=1
            n=str(n)
            for i in n:
                ans*=int(i)
            return ans
        while p(n)%t!=0:
            n+=1
        return n