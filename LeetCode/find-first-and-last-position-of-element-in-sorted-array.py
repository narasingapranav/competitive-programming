class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occur,last_occur=-1,-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                first_occur=mid
                high=mid-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                last_occur=mid
                low=mid+1
        return [first_occur,last_occur]