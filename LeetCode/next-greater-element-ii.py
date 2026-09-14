class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        temp=nums+nums
        n=len(nums)
        res=[-1]*n
        for i in range(n):
            for j in range(i+1,2*n):
                if nums[i]<nums[j%n]:
                    res[i]=nums[j%n]
                    break
        return res