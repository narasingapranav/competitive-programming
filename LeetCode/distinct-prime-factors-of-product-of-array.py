class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            factor = 2
            while factor * factor <= num:
                while num % factor == 0:
                    result.add(factor)
                    num //= factor
                factor += 1
            if num > 1:
                result.add(num)
        return len(result)