# 🟠 minimum-path-sum — Minimum Path Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-path-sum/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Accepted solution for Minimum Path Sum on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Dynamic programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n²) (estimated -- DP table detected)` | `~O(n) (estimated)` |

## 🏷️ Tags

`dp`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        dp=[[0]*c for i in range(r)]
        dp[0][0]=grid[0][0]
        for a in range(1,r):
            dp[a][0]=dp[a-1][0]+grid[a][0]
        for b in range(1,c):
            dp[0][b]=dp[0][b-1]+grid[0][b]
        for a in range(1,r):
            for b in range(1,c):
                dp[a][b]=min(dp[a-1][b],dp[a][b-1])+grid[a][b]
        return dp[-1][-1]
         
```

</details>
