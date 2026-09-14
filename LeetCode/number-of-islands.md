# 🟠 number-of-islands — Number of Islands

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-islands/) &nbsp;|&nbsp; **Solved:** 2025-12-18

---

## 📝 Summary

Accepted solution for Number of Islands on LeetCode.

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
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        def dfs(r,c):
            d=[(1,0),(-1,0),(0,1),(0,-1)]
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return
            if visited[r][c] or grid[r][c]=='0':
                return
            visited[r][c]=True
            for dr,dc in d:
                dfs(r+dr,c+dc)
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and not visited[i][j]:
                    dfs(i,j)
                    c+=1
        return c

```

</details>
