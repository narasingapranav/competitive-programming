from math import gcd
from collections import Counter
from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter()
        for num in nums:
            g = gcd(num, k)
            for prev_g in count:
                if (g * prev_g) % k == 0:
                    ans += count[prev_g]
            count[g] += 1
        return ans