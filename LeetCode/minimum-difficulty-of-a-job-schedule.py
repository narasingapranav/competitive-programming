class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1
        dp = [[10000000] * (n) for _ in range(d + 1)]
        maxjob = 0
        for i in range(n):
            maxjob = max(maxjob, a[i])
            dp[1][i] = maxjob
        for day in range(2, d + 1):
            for i in range(day - 1, n):
                maxjob = 0
                for j in range(i, day - 2, -1):
                    maxjob = max(maxjob, a[j])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + maxjob)
        return dp[d][n - 1]
