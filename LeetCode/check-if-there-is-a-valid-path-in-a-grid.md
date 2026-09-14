# 🟠 check-if-there-is-a-valid-path-in-a-grid — Check if There is a Valid Path in a Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) &nbsp;|&nbsp; **Solved:** 2026-04-27

---

## 📝 Summary

Accepted solution for Check if There is a Valid Path in a Grid on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS) + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`graph` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if not grid:
            return true
        directions = {1: [(0,-1),(0,1)],
                      2: [(-1,0),(1,0)],
                      3: [(0,-1),(1,0)],
                      4: [(0,1),(1,0)],
                      5: [(0,-1),(-1,0)],
                      6: [(0,1),(-1,0)]}
        visited = set()
        goal = (len(grid)-1, len(grid[0]) - 1)
        def dfs(i, j):
            visited.add((i,j))
            if (i,j) == goal:
                return True
            for d in directions[grid[i][j]]:
                ni, nj = i+d[0], j+d[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited and (-d[0], -d[1]) in directions[grid[ni][nj]]:
                    if dfs(ni, nj):
                        return True
            return False
        return dfs(0,0)
```

</details>
