from itertools import combinations
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for bit in range(32):
            ones = 0
            mask = 1 << bit
            for num in nums:
                if num & mask:
                    ones += 1

            zeros = n - ones
            ans += ones * zeros

        return ans