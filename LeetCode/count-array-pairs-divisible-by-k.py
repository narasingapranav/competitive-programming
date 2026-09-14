from math import gcd
from collections import Counter
from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter()
        for num in nums:
            g = gcd(num, k)
            for i in count:
                if (g * i) % k == 0:
                    ans += count[i]
            count[g] += 1
        return ans