class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[bin(i) for i in range(n+1)]
        c=[]
        for i in a:
            c.append(i.count('1'))
        return c