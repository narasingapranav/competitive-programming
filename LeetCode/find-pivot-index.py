class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:])==0:
            return 0
        for i in range(1,len(nums)):
           ls=sum(nums[:i])
           rs=sum(nums[(i+1):])
           if ls==rs:
                return i
        return -1