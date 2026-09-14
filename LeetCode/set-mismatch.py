class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set()
        duplicate = -1
        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)
        total_sum = n * (n + 1) // 2
        missing = total_sum - (sum(nums) - duplicate)
        
        return [duplicate, missing]