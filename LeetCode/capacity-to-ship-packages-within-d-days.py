class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def solve(wei):
            total=1
            w=0
            for i in weights:
                if w+i>wei:
                    total+=1
                    w=i
                else:
                    w+=i
            return total
        l=max(weights)
        h=sum(weights)
        while l<=h:
            mid=l+(h-l)//2
            if solve(mid)>days:
                l=mid+1
            else:
                h=mid-1
        return l