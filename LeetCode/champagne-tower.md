# 🟠 champagne-tower — Champagne Tower

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/champagne-tower/) &nbsp;|&nbsp; **Solved:** 2026-02-14

---

## 📝 Summary

Accepted solution for Champagne Tower on LeetCode.

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
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * 101 for _ in range(101)]
        dp[0][0] = poured

        for row in range(query_row):
            for col in range(row + 1):
                if dp[row][col] > 1:
                    overflow = (dp[row][col] - 1) / 2.0
                    dp[row + 1][col] += overflow
                    dp[row + 1][col + 1] += overflow
                    dp[row][col] = 1  

        return min(1, dp[query_row][query_glass])

```

</details>
