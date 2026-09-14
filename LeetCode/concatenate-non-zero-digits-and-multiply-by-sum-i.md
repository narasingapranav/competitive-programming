# 🟠 concatenate-non-zero-digits-and-multiply-by-sum-i — Concatenate Non-Zero Digits and Multiply by Sum I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/) &nbsp;|&nbsp; **Solved:** 2026-07-07

---

## 📝 Summary

Accepted solution for Concatenate Non-Zero Digits and Multiply by Sum I on LeetCode.

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
    def sumAndMultiply(self, n: int) -> int:
        if n==0 : return 0
        s=""
        su=0
        for i in str(n):
            if i!="0":
                s+=i
                su+=int(i)
        s=int(s)
        return s*su

```

</details>
