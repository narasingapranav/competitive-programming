# 🟠 stone-game-ii — Stone Game II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/stone-game-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Determine the maximum number of stones Alice can collect in a game where players can take X piles (1 <= X <= 2M) per turn and update M = max(M, X), starting with M = 1.

## 🔍 Key Observation

The maximum stones a player can obtain starting at pile i with parameter M equals the total remaining stones minus the opponent's optimal score from pile i + X with parameter max(M, X).

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^3)` | `O(n^2)` |

## 🏷️ Tags

`dynamic-programming` `game-theory` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix[i]
                    continue
                for x in range(1, 2 * m + 1):
                    dp[i][m] = max(dp[i][m],suffix[i] - dp[i + x][max(m, x)])
        return dp[0][1]
```

</details>
