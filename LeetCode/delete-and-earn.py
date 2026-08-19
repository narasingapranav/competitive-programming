class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq=Counter(nums)
        m=max(nums)
        dp=[0]*(m+1)
        dp[0]=0
        dp[1]=freq[1]*1
        for i in range(2,m+1):
            dp[i]=max(dp[i-1],freq[i]*i+dp[i-2])
        return dp[m]