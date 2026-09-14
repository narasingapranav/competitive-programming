class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * 101 for _ in range(101)]
        dp[0][0] = poured

        for row in range(query_row):
            for col in range(row + 1):
                if dp[row][col] > 1:
                    overflow = (dp[row][col] - 1) / 2.0
                    dp[row + 1][col] += overflow
                    dp[row + 1][col + 1] += overflow
                    dp[row][col] = 1  

        return min(1, dp[query_row][query_glass])
