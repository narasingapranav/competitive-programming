class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_val = max(nums)
        num_set = set(nums)
        ans = 0
        for x in range(1, max_val + 1):
            g = 0
            for multiple in range(x, max_val + 1, x):
                if multiple in num_set:
                    g = self.gcd(g, multiple)
                if g == x:
                    ans += 1
                    break
        return ans