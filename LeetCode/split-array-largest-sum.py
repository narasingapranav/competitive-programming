class Solution:
    def func(self,nums,mid):
        a=1
        s=0
        for i in range(len(nums)):
            if s+nums[i]<=mid:
                s+=nums[i]
            else:
                a+=1
                s=nums[i]
        return a
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums)==k:
            return max(nums)
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid= low+ (high-low)//2
            splits=self.func(nums,mid)
            if splits<=k:
                high=mid-1
            else:
                low=mid+1
        return low