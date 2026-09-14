class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=nums[l]:
                if nums[mid]>nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[mid]<nums[r]:
                r=mid
        return nums[l]'''
        if target in nums:
            return nums.index(target)
        else:
            return -1