# 🟠 shift-2d-grid — Shift 2D Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/shift-2d-grid/) &nbsp;|&nbsp; **Solved:** 2026-07-20

---

## 📝 Summary

Accepted solution for Shift 2D Grid on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def shift(self,grid):
        lastrow=[grid[i][-1] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])-1,0,-1):
                grid[i][j]=grid[i][j-1]
        for i in range(1,len(grid)):
            grid[i][0]=lastrow[i-1]
        grid[0][0]=lastrow[-1]
        return grid
                
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        while k>0:
            self.shift(grid)
            k-=1
        return grid
```

</details>
