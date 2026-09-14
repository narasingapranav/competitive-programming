# 🟠 power-of-four — Power of Four

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/power-of-four/) &nbsp;|&nbsp; **Solved:** 2025-08-15

---

## 📝 Summary

Accepted solution for Power of Four on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and (n & (n-1))==0 and (n & 0xAAAAAAAA) == 0
```

</details>
