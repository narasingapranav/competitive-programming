# 🟠 dungeon-game — Dungeon Game

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/dungeon-game/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Accepted solution for Dungeon Game on LeetCode.

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
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        dp=[[0]*n for _ in range(m)]
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        for i in range(m-2,-1,-1):
            need = dp[i+1][n-1]
            dp[i][n-1] = max(1, need - dungeon[i][n-1])
        for j in range(n-2,-1,-1):
            need = dp[m-1][j+1]
            dp[m-1][j] = max(1, need - dungeon[m-1][j])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                need = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, need - dungeon[i][j])
        return dp[0][0]
```

</details>
