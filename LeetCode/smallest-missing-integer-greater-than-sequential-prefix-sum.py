class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        su=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                su+=nums[i]
            else:
                break
        while su in nums:
            su+=1
        return su