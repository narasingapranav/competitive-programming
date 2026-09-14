# 🟠 calculate-money-in-leetcode-bank — Calculate Money in Leetcode Bank

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/calculate-money-in-leetcode-bank/) &nbsp;|&nbsp; **Solved:** 2025-09-02

---

## 📝 Summary

Accepted solution for Calculate Money in Leetcode Bank on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total = 0
        for i in range(weeks):
            total += (7 * (2*i + 1 + 7)) // 2
        start = weeks + 1
        for i in range(days):
            total += start + i

        return total

```

</details>
