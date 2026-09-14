class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            hrs=0
            for i in piles:
                hrs+=math.ceil(i/mid)
            if hrs>h:
                low=mid+1
            else:
                high=mid-1
        return low
