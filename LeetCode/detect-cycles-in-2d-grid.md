# 🟠 detect-cycles-in-2d-grid — Detect Cycles in 2D Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/detect-cycles-in-2d-grid/) &nbsp;|&nbsp; **Solved:** 2026-04-26

---

## 📝 Summary

Accepted solution for Detect Cycles in 2D Grid on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dirs = [(0,1), (0, -1), (1,0), (-1,0)]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def detect(x1, y1, p1, p2, prev):
            visited[x1][y1] = True
            for x2, y2 in dirs:
                x = x1+x2
                y = y1+y2
                if (x2 != (-1*p1) or y2 != (-1*p2)) and x >= 0 and x < m and y >=0 and y < n and prev == grid[x][y]:
                    if visited[x][y] or detect(x,y,x2,y2, prev):
                        return True
            return False
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if detect(i, j, -1, -1, grid[i][j]):
                        return True 
        return False
```

</details>
