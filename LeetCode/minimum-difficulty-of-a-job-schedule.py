class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1
        dp = [[10000000] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0
        for day in range(1, d + 1):
            for i in range(day, n + 1):
                maxjob = 0
                for j in range(i - 1, day - 2, -1):
                    maxjob = max(maxjob, a[j])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j] + maxjob)
        return dp[d][n]
