from collections import deque

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        NEG = -10**30

        prev = [0] * (n + 1)  # dp[0][i] = 0
        answer = NEG

        for t in range(1, m + 1):
            cur = [NEG] * (n + 1)
            dq = deque()

            for i in range(1, n + 1):

                # Add j = i - l into the candidate window
                add_j = i - l
                if add_j >= 0:
                    val = prev[add_j] - pref[add_j]

                    while dq and dq[-1][1] <= val:
                        dq.pop()
                    dq.append((add_j, val))

                # Remove j < i - r
                while dq and dq[0][0] < i - r:
                    dq.popleft()

                # Option 1: don't end a subarray at i
                cur[i] = cur[i - 1]

                # Option 2: end the t-th subarray at i
                if dq:
                    cur[i] = max(cur[i], pref[i] + dq[0][1])

            answer = max(answer, cur[n])
            prev = cur

        return answer