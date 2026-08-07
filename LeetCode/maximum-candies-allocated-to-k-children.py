class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        h=max(candies)
        while l<=h:
            mid=l+(h-l)//2
            ans=sum([i//mid for i in candies])
            if ans>=k:
                l=mid+1
            else:
                h=mid-1
        return h