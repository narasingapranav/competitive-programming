from itertools import combinations
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        a=float('inf')
        for i in range(len(nums)-k+1):
            a=min(a,nums[i+k-1]-nums[i])
        return a