class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        from typing import List
        MOD = 10**9 + 7
        n = len(parent)

        g = [[] for _ in range(n)]

        for i in range(1, n):
            g[parent[i]].append(i)

        def merge(A, B):
            res = [0] * k

            for i in range(k):
                if A[i] == 0:
                    continue

                for j in range(k):
                    if B[j] == 0:
                        continue

                    res[(i + j) % k] += A[i] * B[j]
                    res[(i + j) % k] %= MOD

            return res

        def dfs(u):

            # u not selected
            dp0 = [0] * k
            dp0[0] = 1

            # u selected
            dp1 = [0] * k
            dp1[nums[u] % k] = 1

            for v in g[u]:

                c0, c1 = dfs(v)

                # if u not selected
                all_child = [
                    (c0[i] + c1[i]) % MOD
                    for i in range(k)
                ]

                ndp0 = merge(dp0, all_child)

                # if u selected
                ndp1 = merge(dp1, c0)

                dp0 = ndp0
                dp1 = ndp1

            return dp0, dp1

        dp0, dp1 = dfs(0)

        return (dp0[0] + dp1[0] - 1) % MOD