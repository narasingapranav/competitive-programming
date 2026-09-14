from functools import lru_cache
class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:


        def get_sum(limit: int) -> int:
            if limit < 0:
                return 0

            @lru_cache(None)
            def dp(pos: int, tight: bool):
                if pos < 0:
                    return (1, 0)  # (count, sum)

                max_bit = (limit >> pos) & 1 if tight else 1

                total_count = 0
                total_sum = 0

                for bit in range(max_bit + 1):
                    # If n has a 1 here, x cannot have a 1 here
                    if ((n >> pos) & 1) and bit:
                        continue

                    cnt, sm = dp(
                        pos - 1,
                        tight and (bit == max_bit)
                    )

                    total_count += cnt
                    total_sum += sm + cnt * (bit << pos)

                return (total_count, total_sum)

            return dp(60, True)[1]

        left = max(1, n - k)
        right = n + k

        return get_sum(right) - get_sum(left - 1)