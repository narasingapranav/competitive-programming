# 🟠 find-the-safest-path-in-a-grid — Find the Safest Path in a Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Find a path from the top-left to the bottom-right of a grid that maximizes the minimum Manhattan distance from any cell on the path to the nearest thief.

## 🔍 Key Observation

Precompute the distance to the nearest thief for all grid cells using multi-source BFS, then use Dijkstra's algorithm to find a path that maximizes the bottleneck cell distance.

## ⚙️ Algorithm

**Multi-source BFS + Dijkstra's algorithm**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2 log n)` | `O(n^2)` |

## 🏷️ Tags

`multi-source-bfs` `dijkstra` `grid` `graph` `priority-queue`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    def maximumSafenessFactor(self, A: List[List[int]]) -> int:
        if A[0][0] or A[-1][-1]: return 0
        n, q = len(A), deque()
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            v = A[i][j]
            for dx, dy in self.dirs:
                x, y = i + dx, j + dy
                if min(x, y) >= 0 and max(x, y) < n and not A[x][y]:
                    A[x][y] = v + 1
                    q.append((x, y))
        pq = [(-A[0][0], 0, 0)]
        while pq:
            sf, i, j = heapq.heappop(pq)
            sf = -sf
            if i == n - 1 and j == n - 1:
                return sf - 1
            for dx, dy in self.dirs:
                x, y = i + dx, j + dy
                if min(x, y) >= 0 and max(x, y) < n and A[x][y] > 0:
                    heapq.heappush(pq, (-min(sf, A[x][y]), x, y))
                    A[x][y] *= -1
        return A[n - 1][n - 1] - 1
```

</details>
