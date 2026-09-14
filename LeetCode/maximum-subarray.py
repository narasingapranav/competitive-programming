class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mf=nums[0]
        cm=nums[0]
        for i in range(1,len(nums)):
            cm=max(nums[i],cm+nums[i])
            mf=max(mf,cm)
        return mf