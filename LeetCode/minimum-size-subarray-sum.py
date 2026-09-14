class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        n=len(nums)
        m=float('inf')
        s=0
        for r in range(n):
            s+=nums[r]
            while s>=target:
                m=min(m,r-l+1)
                s=s-nums[l]
                l+=1
        return 0 if m==float('inf') else m