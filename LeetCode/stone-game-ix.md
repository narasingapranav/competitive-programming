# 🟠 stone-game-ix — Stone Game IX

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/stone-game-ix/) &nbsp;|&nbsp; **Solved:** 2026-08-16

---

## 📝 Summary

Determine if Alice can win a turn-based game where players remove stones such that the running sum of picked stone values is never divisible by 3.

## 🔍 Key Observation

The game outcome depends solely on the counts of stone values modulo 3: stones with remainder 0 delay turns without changing remainder parity, while relative counts of stones with remainders 1 and 2 dictate force-win strategies.

## ⚙️ Algorithm

**Game Theory / Case Analysis**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`game-theory` `math` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def stoneGameIX(self, a: List[int]) -> bool:
        z = Counter(v%3 for v in a)
        return (z[1]>0<z[2],abs(z[1]-z[2])>2)[z[0]&1]
```

</details>
