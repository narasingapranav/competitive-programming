# 🟠 longest-increasing-path-in-a-matrix — Longest Increasing Path in a Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) &nbsp;|&nbsp; **Solved:** 2026-05-03

---

## 📝 Summary

Accepted solution for Longest Increasing Path in a Matrix on LeetCode.

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
    def dfs(self,mat,i,j,table):
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        m,n=len(mat),len(mat[0])
        maxlen=1
        if table[i][j] != -1:
            return table[i][j]
        for dx,dy in dirs:
            nx,ny=i+dx,j+dy
            if nx>=0 and ny>=0 and nx<m and ny<n and mat[nx][ny]>mat[i][j]:
                maxlen=max(maxlen,1+self.dfs(mat,nx,ny,table))
        table[i][j]=maxlen
        return maxlen
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        longpl=0
        table = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                longpl=max(longpl,self.dfs(matrix,i,j,table))
        return longpl       
```

</details>
