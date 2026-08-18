# 🟠 making-a-large-island — Making A Large Island

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/making-a-large-island/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Given a binary grid, find the size of the largest island that can be formed by changing at most one '0' to a '1'.

## 🔍 Key Observation

Assigning a unique ID and area to each connected island allows us to evaluate flipping any '0' cell in O(1) time by summing the areas of its unique adjacent island IDs.

## ⚙️ Algorithm

**DFS / Connected Components**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n^2)` |

## 🏷️ Tags

`dfs` `grid` `connected-components` `graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j,ids):
            if i<0 or j<0 or j>=len(grid[0]) or i>=len(grid) or grid[i][j]!=1:
                return 0   
            grid[i][j]=ids
            return 1+dfs(grid,i,j-1,ids)+dfs(grid,i,j+1,ids)+dfs(grid,i+1,j,ids)+dfs(grid,i-1,j,ids)
        n=len(grid)
        ids=2
        c=0
        res=0
        count=[0]*(n*n+3)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    ids += 1
                    count[ids] = dfs(grid, i, j, ids)
                    res = max(res, count[ids])
                else:
                    c+=1
        if c==0:
            return res
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    c=1
                    seen=set()
                    dirs=[(0,1),(1,0),(-1,0),(0,-1)]
                    for di,dj in dirs:
                        ni=i+di
                        nj=j+dj
                        if n>ni>=0 and n>nj>=0 and grid[ni][nj]!=0:
                            if grid[ni][nj] not in seen:
                                seen.add(grid[ni][nj])
                                c+=count[grid[ni][nj]]
                    res=max(res,c)
        return res
```

</details>
