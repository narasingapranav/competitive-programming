class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprc=float('inf')
        maxpro=0
        for i in prices:
            minprc=min(minprc,i)
            pro=i-minprc
            maxpro=max(maxpro,pro)
        return maxpro