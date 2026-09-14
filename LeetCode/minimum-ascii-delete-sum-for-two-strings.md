# 🟠 minimum-ascii-delete-sum-for-two-strings — Minimum ASCII Delete Sum for Two Strings

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) &nbsp;|&nbsp; **Solved:** 2026-01-10

---

## 📝 Summary

Accepted solution for Minimum ASCII Delete Sum for Two Strings on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Dynamic programming**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n²) (estimated -- DP table detected)` | `~O(n) (estimated)` |

## 🏷️ Tags

`dp`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, j):
            if i == len(s1):
                return sum(ord(c) for c in s2[j:])
            if j == len(s2):
                return sum(ord(c) for c in s1[i:])
            
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            return min(
                ord(s1[i]) + dp(i + 1, j),
                ord(s2[j]) + dp(i, j + 1)
            )
        return dp(0, 0)
        
```

</details>
