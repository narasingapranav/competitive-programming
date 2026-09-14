class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def solveMem(i):
            if dp[i] != -1:
                return dp[i]

            ans = 1

            # move right
            for j in range(i + 1, min(i + d, n - 1) + 1):
                if arr[j] >= arr[i]:
                    break

                ans = max(ans, 1 + solveMem(j))

            # move left
            for j in range(i - 1, max(0, i - d) - 1, -1):
                if arr[j] >= arr[i]:
                    break

                ans = max(ans, 1 + solveMem(j))

            dp[i] = ans
            return dp[i]

        ans = 1

        for i in range(n):
            ans = max(ans, solveMem(i))

        return ans