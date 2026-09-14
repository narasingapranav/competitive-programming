class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #return(nums.index(max(nums)))
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid+1]<nums[mid]:
                r=mid
            elif nums[mid+1]>nums[mid]:
                l=mid+1
        return l