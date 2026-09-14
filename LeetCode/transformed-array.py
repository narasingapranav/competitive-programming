class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i, x in enumerate(nums):
            if x != 0:
                new_idx = (i + (x % n) + n) % n
                result[i] = nums[new_idx]
            else:
                result[i] = 0
        return result
   