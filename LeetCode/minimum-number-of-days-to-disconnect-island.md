# 🟠 minimum-number-of-days-to-disconnect-island — Minimum Number of Days to Disconnect Island

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) &nbsp;|&nbsp; **Solved:** 2026-03-05

---

## 📝 Summary

Accepted solution for Minimum Number of Days to Disconnect Island on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0
        disc = [[-1] * cols for _ in range(rows)]
        low = [[-1] * cols for _ in range(rows)]
        parent = [[-1] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        island_size = 0
        articulation_points = 0

        def dfs(row, col):
            nonlocal time, island_size, articulation_points

            disc[row][col] = low[row][col] = time
            time += 1
            island_size += 1
            children = 0

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue

                if grid[new_row][new_col] == 0:
                    continue

                if disc[new_row][new_col] == -1:
                    parent[new_row][new_col] = row * cols + col
                    children += 1
                    dfs(new_row, new_col)
                    low[row][col] = min(low[new_row][new_col], low[row][col])

                    if parent[row][col] != -1 and low[new_row][new_col] >= disc[row][col]:
                        articulation_points += 1

                elif parent[row][col] != new_row * cols + new_col:
                    low[row][col] = min(low[new_row][new_col], low[row][col])

            if parent[row][col] == -1 and children > 1:
                articulation_points += 1


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and disc[row][col] == -1:
                    if islands == 1:
                        return 0

                    dfs(row, col)
                    islands += 1

        if islands == 0:
            return 0

        if island_size <= 2:
            return island_size

        if articulation_points > 0:
            return 1

        return 2
```

</details>
