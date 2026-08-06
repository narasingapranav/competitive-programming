# 🟠 stone-game-iii — Stone Game III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/stone-game-iii/) &nbsp;|&nbsp; **Solved:** 2026-08-05

---

## 📝 Summary

Determine the winner ('Alice', 'Bob', or 'Tie') of a game where two players alternate taking 1, 2, or 3 stones from the front of an array, both playing optimally to maximize their total score.

## 🔍 Key Observation

The problem can be modeled as finding the maximum score difference (current player minus opponent); from index i, taking k stones yields a net gain of the sum of those k stones minus the optimal score difference achievable by the opponent starting from index i + k.

## ⚙️ Algorithm

**Dynamic programming / Minimax**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`dynamic-programming` `game-theory` `memoization`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    s = ["Bob", "Tie", "Alice"]
    def stoneGameIII(self, A: List[int]) -> str:
        n = len(A)
        @cache
        def maxDiff(i: int) -> int:
            if i == n: return 0
            a = b = c = -5e7
            if i < n:
                a = A[i] - maxDiff(i + 1)
            if i + 1 < n:
                b = A[i] + A[i + 1] - maxDiff(i + 2)
            if i + 2 < n:
                c = A[i] + A[i + 1] + A[i + 2] - maxDiff(i + 3)
            return max(a, b, c)
        d = maxDiff(0)
        return self.s[(d > 0) - (d < 0) + 1]
```

</details>
