# 🟠 distinct-subsequences-ii — Distinct Subsequences II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/distinct-subsequences-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-07

---

## 📝 Summary

Count the number of distinct non-empty subsequences of a given string modulo 10^9 + 7.

## 🔍 Key Observation

Appending a character doubles the total number of subsequences, but to prevent duplicates, we must subtract the number of distinct subsequences that existed prior to its previous occurrence.

## ⚙️ Algorithm

**Dynamic Programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`dynamic-programming` `string` `combinatorics`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        last = {}
        for ch in s:
            old = dp
            dp = 2 * dp - last.get(ch, 0)
            last[ch] = old
            dp %= MOD
        return (dp - 1)%MOD
```

</details>
