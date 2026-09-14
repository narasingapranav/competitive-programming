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
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python

import numpy as np
class Solution:
    def shift(self,grid):
        m,n=len(grid),len(grid[0])
        grid=np.array(grid)
        grid=grid.flatten()
        grid = np.concatenate(([grid[-1]], grid[:-1]))
        grid=grid.reshape(m,n)
        return grid
                
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid=np.array(grid)
        while k>0:
            grid=self.shift(grid)
            k-=1
        return grid.tolist()
```

</details>
