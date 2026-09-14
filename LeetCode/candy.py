class Solution:
    def candy(self, rating: List[int]) -> int:
        n=len(rating)
        dp=[1]*n
        for i in range(1,n):
            if rating[i]>rating[i-1]:
                dp[i]=dp[i-1]+1
        for i in range(n-2,-1,-1):
            if rating[i+1]<rating[i]:
                dp[i]=max(dp[i],dp[i+1]+1)
        return sum(dp)