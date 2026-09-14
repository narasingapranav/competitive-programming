class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        mod, c1, c2, res = 10 ** 9 + 7, 0, 0, 0
        for x in nums:
            if x < a:
                res = (res + c1 + c2) % mod
            elif x <= b:
                res = (res + c2) % mod
                c1 += 1
            else:
                c2 += 1
        return res