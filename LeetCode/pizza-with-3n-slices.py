class Solution:
    def dp(self, slices: List[int], m: int) -> int:
        n = len(slices)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1:
                    dp[i][j] = slices[0]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i - 1])
        
        return dp[n][m]
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        return max(self.dp(slices[:-1], n // 3), self.dp(slices[1:], n // 3))