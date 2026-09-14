class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num == 2:
                result.append(-1)
            else:
                leadingOne = 1
                while (num & leadingOne) > 0:
                    leadingOne <<= 1
                result.append(num - (leadingOne >> 1))
        return result