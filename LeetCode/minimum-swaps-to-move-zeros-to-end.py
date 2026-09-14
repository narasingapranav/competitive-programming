class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n=len(nums)
        z=nums.count(0)
        a=0
        for i in range(n-z,n):
            if nums[i]==0:
                a+=1
        return z-a