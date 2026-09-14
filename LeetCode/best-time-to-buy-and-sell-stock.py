class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mip=float('inf')
        maxpro=0
        for i in prices:
            mip=min(mip,i)
            p=i-mip
            maxpro=max(maxpro,p)
        return maxpro