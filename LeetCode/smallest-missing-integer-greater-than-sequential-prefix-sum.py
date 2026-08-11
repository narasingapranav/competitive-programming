class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        su=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                su+=nums[i]
            else:
                break
        s=set(nums)
        while su in s:
            su+=1
        return su