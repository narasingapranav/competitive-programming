# 🟠 number-of-islands — Number of Islands

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-islands/) &nbsp;|&nbsp; **Solved:** 2026-07-22

---

## 📝 Summary

Accepted solution for Number of Islands on LeetCode.

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
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        m=len(grid)
        n=len(grid[0])
        vis=[[False]*n for _ in range(m)]
        def dfs(i,j):
            if i>=m or j>=n or i <0 or j<0 or vis[i][j] or grid[i][j]=='0':
                return 
            vis[i][j]=True
            dirs=[(0,-1),(0,1),(-1,0),(1,0)]
            for di,dj in dirs:
                ni,nj=i+di,j+dj
                dfs(ni,nj)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not vis[i][j]:
                    dfs(i,j)
                    count+=1
        return count
```

</details>
