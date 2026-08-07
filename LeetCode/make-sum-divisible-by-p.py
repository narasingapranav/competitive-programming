class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalrem=sum(nums)%p
        if totalrem==0:
            return 0
        ps=[0]*len(nums)
        ps[0]=nums[0]%p
        for i in range(1,len(nums)):
            ps[i]=(ps[i-1]+nums[i])%p
        m=len(nums)
        d={0:-1}
        for i in range(len(ps)):
            cr=ps[i]
            pr=(cr-totalrem+p)%p
            if pr in d:
                m=min(m,i-d[pr])
            d[cr]=i
        return -1 if m==len(nums) else m

