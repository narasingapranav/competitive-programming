class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD=10**9 + 7
        res=k
        ops=0
        for i in nums:
            if res<i:
                req=(i-res+k-1)//k
                ops+=req
                res+=req*k
            res-=i
        return (ops*(ops+1)//2)%MOD
                