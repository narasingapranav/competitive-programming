# 🟠 reverse-integer — Reverse Integer

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-integer/) &nbsp;|&nbsp; **Solved:** 2025-07-08

---

## 📝 Summary

Accepted solution for Reverse Integer on LeetCode.

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
    def reverse(self, x: int) -> int:
        max=2**31-1
        min=-2**31
        rev,sign=0,1
        if x<0:
            sign=-1
            x=-x
        while(x>0):
           while x > 0:
            digit = x % 10
            x //= 10
            if rev > (max - digit) // 10:
                return 0
            rev = rev * 10 + digit
        return rev * sign
```

</details>
