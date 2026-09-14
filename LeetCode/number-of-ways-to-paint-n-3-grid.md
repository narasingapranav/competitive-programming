# 🟠 number-of-ways-to-paint-n-3-grid — Number of Ways to Paint N × 3 Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/) &nbsp;|&nbsp; **Solved:** 2026-01-03

---

## 📝 Summary

Accepted solution for Number of Ways to Paint N × 3 Grid on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        same = 6
        diff = 6 
        for _ in range(2, n + 1):
            new_same = (same * 3 + diff * 2) % MOD
            new_diff = (same * 2 + diff * 2) % MOD
            same, diff = new_same, new_diff
        return (same + diff) % MOD

```

</details>
