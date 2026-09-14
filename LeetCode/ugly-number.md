# 🟠 ugly-number — Ugly Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/ugly-number/) &nbsp;|&nbsp; **Solved:** 2026-05-27

---

## 📝 Summary

Accepted solution for Ugly Number on LeetCode.

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
    def isUgly(self, n: int) -> bool:
        if  n<=0:
            return False
        for prime in [2,3,5]:
            while n%prime==0:
                n//=prime
        return n==1
```

</details>
