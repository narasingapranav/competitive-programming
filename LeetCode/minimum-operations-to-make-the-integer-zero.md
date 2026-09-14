# 🟠 minimum-operations-to-make-the-integer-zero — Minimum Operations to Make the Integer Zero

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/) &nbsp;|&nbsp; **Solved:** 2025-09-05

---

## 📝 Summary

Accepted solution for Minimum Operations to Make the Integer Zero on LeetCode.

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
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # try operations count
            val = num1 - k * num2
            if val < 0:
                return -1
            if bin(val).count("1") <= k <= val:
                return k
        return -1
```

</details>
