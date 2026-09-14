# 🟠 string-to-integer-atoi — String to Integer (atoi)

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/string-to-integer-atoi/) &nbsp;|&nbsp; **Solved:** 2025-08-16

---

## 📝 Summary

Accepted solution for String to Integer (atoi) on LeetCode.

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
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = -1 if s[:1] == '-' else 1
        if s[:1] in '-+': s = s[1:]
        num = 0
        for c in s:
            if not c.isdigit(): break
            num = num * 10 + int(c)
        num *= sign
        return max(-2**31, min(num, 2**31 - 1))
```

</details>
