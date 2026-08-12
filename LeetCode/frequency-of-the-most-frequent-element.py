class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        x=k
        nums.sort()
        for r in range(len(nums)):
            x+=nums[r]
            if x<nums[r]*(r-l+1):
                x-=nums[l]
                l+=1
        return len(nums)-l