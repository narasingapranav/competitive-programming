class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        ans=float('inf')
        for x in range(k):
            for y in range(k):
                if x==y:
                    continue
                cost=0
                for i in range(n):
                    target=x if i%2==0 else y
                    r=nums[i]%k
                    cost+=min((r-target)%k,(target-r)%k)
                ans=min(ans,cost)
        return ans