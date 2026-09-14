class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []

        def dfs(i: int, cost: int, prev_one: bool, path: list):
            if cost > k:
                return

            if i == n:
                ans.append("".join(path))
                return

            # Place '0'
            path.append('0')
            dfs(i + 1, cost, False, path)
            path.pop()

            # Place '1'
            if not prev_one and cost + i <= k:
                path.append('1')
                dfs(i + 1, cost + i, True, path)
                path.pop()

        dfs(0, 0, False, [])
        return ans