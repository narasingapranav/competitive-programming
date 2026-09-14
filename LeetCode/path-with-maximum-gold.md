# 🟠 path-with-maximum-gold — Path with Maximum Gold

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/path-with-maximum-gold/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Path with Maximum Gold on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def dfs(self,grid,x,y):
        n,m=len(grid),len(grid[0])
        # check for out of bounds if yes 0
        if x<0 or x>=n or y<0 or y>=m or grid[x][y]==0: 
            return 0
        # store present value useful in BT
        curgold=grid[x][y]
        # take the present gold value and add to res
        grid[x][y]=0
        localmax=curgold
        dirs=[(1,0),(-1,0),(0,-1),(0,1)]
        # dfs
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            localmax=max(localmax,curgold+self.dfs(grid,nx,ny)) # find max of present and dfs
        # backtrack i.e, restore old value
        grid[x][y]=curgold
        return localmax
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # idea : traverse full matrix and perform dfs if not 0 return max gold
        maxg=0
        n,m=len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    maxg=max(maxg,self.dfs(grid,i,j))
        return maxg
        
```

</details>
