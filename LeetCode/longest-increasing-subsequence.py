class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bs(dp,n,target):
            l=0
            h=n
            while l<h:
                m=(l+h)//2
                if dp[m]>=target:
                    h=m
                else:
                    l=m+1
            return l
        n=len(nums)
        dp=[0]*(n)
        dp[0]=nums[0]
        size=1
        for i in range(1,n):
            lb=bs(dp,size,nums[i])
            if lb==size:
                size+=1
            dp[lb]=nums[i]
        return size