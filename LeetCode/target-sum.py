class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p = set of positive numbers
        # n = set of negative numbers
        # sum of p + sum of n = sum of nums
        # sum of p - sum of n = target
        # 2*sum of p          = target + sum of nums
        # sum of p            = (target + sum of nums)//2
        s=sum(nums)
        if abs(target)>s: return 0
        if (s+target)%2==1: return 0
        t=(s+target)//2
        dp=[0]*(t+1)
        dp[0]=1
        for i in nums:
            for j in range(t,i-1,-1):
                dp[j]+=dp[j-i]
        return dp[t]