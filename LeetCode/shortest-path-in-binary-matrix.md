# 🟠 shortest-path-in-binary-matrix — Shortest Path in Binary Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix/) &nbsp;|&nbsp; **Solved:** 2026-05-01

---

## 📝 Summary

Accepted solution for Shortest Path in Binary Matrix on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Graph/tree traversal (BFS/DFS)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`graph`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid [0][0]==1:
            return -1
        moves=[(1,0),(0,1),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]
        q=deque([(0,0,1)])
        grid[0][0]=1
        while q:
            x,y,dist=q.popleft()
            if x==n-1 and y==n-1:
                return dist
            for dx,dy in moves:
                nx,ny=x+dx,y+dy
                if 0<=nx <n and 0<=ny<n and grid[nx][ny]==0:
                    grid[nx][ny]=1
                    q.append((nx,ny,dist+1))
        return -1
```

</details>
