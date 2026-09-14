# 🟠 find-the-index-of-the-first-occurrence-in-a-string — Find the Index of the First Occurrence in a String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Accepted solution for Find the Index of the First Occurrence in a String on LeetCode.

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
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        h=len(haystack)
        for i in range(h-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1
```

</details>
