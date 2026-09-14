from typing import List
from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0
        dist = self.getDistance(grid, m, n)
        lo = 0
        hi = m + n
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.canReach(dist, m, n, mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
    def getDistance(self, grid, m, n):
        dist = [[-1] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if dist[ni][nj] == -1:
                        dist[ni][nj] = dist[i][j] + 1
                        q.append((ni, nj))
        return dist
    def canReach(self, dist, m, n, k):
        vis = [[False] * n for _ in range(m)]
        return self.dfs(0, 0, dist, vis, m, n, k)
    def dfs(self, i, j, dist, vis, m, n, k):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if vis[i][j]:
            return False
        if dist[i][j] < k:
            return False
        if i == m - 1 and j == n - 1:
            return True
        vis[i][j] = True
        return (
            self.dfs(i + 1, j, dist, vis, m, n, k) or
            self.dfs(i - 1, j, dist, vis, m, n, k) or
            self.dfs(i, j + 1, dist, vis, m, n, k) or
            self.dfs(i, j - 1, dist, vis, m, n, k)
        )