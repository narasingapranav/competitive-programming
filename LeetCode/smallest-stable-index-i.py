class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            lh=nums[0:(i+1)]
            rh=nums[i:]
            if max(lh)-min(rh)<=k:
                return i
        return -1