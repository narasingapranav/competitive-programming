# 🟠 integer-break — Integer Break

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/integer-break/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Accepted solution for Integer Break on LeetCode.

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
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        if n==3: return 2
        q=n//3
        r=n%3
        if r==0:
            return 3**q
        if r==1:
            return 3**(q-1) * 4
        if r==2:
            return (3**q) * 2
```

</details>
