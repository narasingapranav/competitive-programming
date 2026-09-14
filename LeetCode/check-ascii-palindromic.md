# 🟠 check-ascii-palindromic — Check ASCII Palindromic

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-ascii-palindromic/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Accepted solution for Check ASCII Palindromic on LeetCode.

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
    def isPalindromic(self, s: str) -> bool:
        res=''
        for i in s:
            res += format(ord(i), '08b')
        return res==res[::-1]
```

</details>
