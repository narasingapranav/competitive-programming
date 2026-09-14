# 🟠 valid-palindrome — Valid Palindrome

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/valid-palindrome/) &nbsp;|&nbsp; **Solved:** 2025-08-14

---

## 📝 Summary

Accepted solution for Valid Palindrome on LeetCode.

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
    def isPalindrome(self, s: str) -> bool:
        s="".join(i for i in s if i.isalnum()).lower()
        return s==s[::-1]
```

</details>
