class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        pow2 = 1
        while pow2 < n:
            pow2 <<= 1
        max_k = pow2 - 1
        
        k = max_k
        for i, val in enumerate(nums):
            if val != i:
                k &= val
        
        return 0 if k == max_k else k