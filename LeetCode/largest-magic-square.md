# 🟠 largest-magic-square — Largest Magic Square

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/largest-magic-square/) &nbsp;|&nbsp; **Solved:** 2026-01-21

---

## 📝 Summary

Accepted solution for Largest Magic Square on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^7) (estimated -- 7 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # prefix sums
        prefixRow = [[0]*(n+1) for _ in range(m)]
        prefixCol = [[0]*(m+1) for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                prefixRow[i][j+1] = prefixRow[i][j] + grid[i][j]
                prefixCol[j][i+1] = prefixCol[j][i] + grid[i][j]
        
        def isMagic(i, j, k):
            # i,j is top left of kxk square
            # main diag and anti diag
            diag=0; anti=0
            for d in range(k):
                diag += grid[i+d][j+d]
                anti += grid[i+d][j+k-1-d]
            if diag != anti: 
                return False
            # check rows and columns
            for d in range(k):
                # row sum
                rsum = prefixRow[i+d][j+k] - prefixRow[i+d][j]
                # column sum
                csum = prefixCol[j+d][i+k] - prefixCol[j+d][i]
                if rsum != diag or csum != diag:
                    return False
            return True
        
        # try from max possible k down
        for k in range(min(m,n), 1, -1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if isMagic(i, j, k):
                        return k
        return 1
```

</details>
