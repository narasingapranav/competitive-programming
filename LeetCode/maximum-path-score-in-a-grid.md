# 🟠 maximum-path-score-in-a-grid — Maximum Path Score in a Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-path-score-in-a-grid/) &nbsp;|&nbsp; **Solved:** 2026-04-30

---

## 📝 Summary

Accepted solution for Maximum Path Score in a Grid on LeetCode.

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
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k+1):

                    if dp[i][j][c] == -1:
                        continue

                    # move down
                    if i + 1 < m:
                        val = grid[i+1][j]
                        cost = 0 if val == 0 else 1

                        nc = c + cost
                        if nc <= k:
                            dp[i+1][j][nc] = max(
                                dp[i+1][j][nc],
                                dp[i][j][c] + val
                            )

                    # move right
                    if j + 1 < n:
                        val = grid[i][j+1]
                        cost = 0 if val == 0 else 1

                        nc = c + cost
                        if nc <= k:
                            dp[i][j+1][nc] = max(
                                dp[i][j+1][nc],
                                dp[i][j][c] + val
                            )

        ans = -1
        for c in range(k+1):
            ans = max(ans, dp[m-1][n-1][c])

        return ans
```

</details>
