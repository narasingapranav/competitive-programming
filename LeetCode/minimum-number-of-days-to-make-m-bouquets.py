class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid= low + (high-low)//2
            boq=0
            con=0
            for i in range(0,len(bloomDay)):
                if bloomDay[i]<=mid:
                    con+=1
                    if con==k:
                        boq+=1
                        con=0
                else:
                    con=0
            if boq>=m:
                high=mid-1
            else:
                low=mid+1
        return low
