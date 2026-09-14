# 🟠 unique-paths-iii — Unique Paths III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-paths-iii/) &nbsp;|&nbsp; **Solved:** 2026-02-15

---

## 📝 Summary

Accepted solution for Unique Paths III on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty = 0
        start_x = start_y = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1
                elif grid[r][c] == 1:
                    start_x, start_y = r, c
        def dfs(x, y, remain):
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return 1 if remain == -1 else 0
            temp = grid[x][y]
            grid[x][y] = -1
            paths = (
                dfs(x + 1, y, remain - 1) +
                dfs(x - 1, y, remain - 1) +
                dfs(x, y + 1, remain - 1) +
                dfs(x, y - 1, remain - 1)
            )
            grid[x][y] = temp
            return paths
        return dfs(start_x, start_y, empty)

```

</details>
