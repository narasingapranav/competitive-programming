class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        min1, min2 = float('inf'), float('inf')
        for x in nums[1:]:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
        
        return first + min1 + min2