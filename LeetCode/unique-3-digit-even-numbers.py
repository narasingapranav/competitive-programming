class Solution:
    def totalNumbers(self, a: List[int]) -> int:
        from collections import Counter

        c = Counter(a)
        ans = 0

        for last in [0, 2, 4, 6, 8]:
            if c[last] == 0:
                continue

            c[last] -= 1

            for first in range(1, 10):
                if c[first] == 0:
                    continue

                c[first] -= 1
                ans += sum(1 for x in c if c[x] > 0)
                c[first] += 1

            c[last] += 1

        return ans