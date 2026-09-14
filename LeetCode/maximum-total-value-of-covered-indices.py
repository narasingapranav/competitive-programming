class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        pos = [i for i, ch in enumerate(s) if ch == '1']

        if not pos:
            return 0

        NEG = -10**18

        # dp[pos occupied by previous token]
        dp = {}

        first = pos[0]

        if first == 0:
            dp[0] = nums[0]
        else:
            dp[first - 1] = nums[first - 1]
            dp[first] = nums[first]

        for p in pos[1:]:
            ndp = {}

            for last_pos, cur in dp.items():

                for final_pos in ([p] if p == 0 else [p - 1, p]):
                    add = nums[final_pos]

                    if final_pos == last_pos:
                        add = 0

                    ndp[final_pos] = max(
                        ndp.get(final_pos, NEG),
                        cur + add
                    )

            dp = ndp

        return max(dp.values())