class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        n = len(nums)
        maxi = 0
        for i in range(n):
            if isPrime(nums[i][i]):
                maxi = max(maxi, nums[i][i])
            if isPrime(nums[i][n - 1 - i]):
                maxi = max(maxi, nums[i][n - 1 - i])
        return maxi