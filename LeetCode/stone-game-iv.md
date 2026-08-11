# 🟠 stone-game-iv — Stone Game IV

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/stone-game-iv/) &nbsp;|&nbsp; **Solved:** 2026-08-11

---

## 📝 Summary

Determine if the first player can force a win in a stone-removal game where players take turns removing a non-zero perfect square number of stones from a total of n stones.

## 🔍 Key Observation

A state with i stones is a winning state if the player can transition to at least one losing state (i - s) by removing some valid square number of stones s.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n sqrt(n))` | `O(n)` |

## 🏷️ Tags

`dynamic-programming` `game-theory` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        squares = []
        curSquare = 1
        for i in range(1, n + 1):
            if i == curSquare * curSquare:
                squares.append(i)
                curSquare += 1
                dp[i] = True
            else:
                for square in squares:
                    if not dp[i - square]:
                        dp[i] = True
                        break
        return dp[n]
```

</details>
