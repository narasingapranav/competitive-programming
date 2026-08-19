class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[dict() for _ in range(n)]
        res=0
        for i in range(n):
            for j in range(i):
                d=nums[i]-nums[j]
                c=dp[j].get(d,1)+1
                dp[i][d]=c
                res=max(res,c)
        return res