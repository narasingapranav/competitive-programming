import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        low=1
        high=max(piles)
        while low<high:
            mid= low +(high-low)//2
            a=0
            for i in piles:
                a+=math.ceil(i/mid)
            if a<=h:
                high=mid
            else:
                low=mid+1
        return low