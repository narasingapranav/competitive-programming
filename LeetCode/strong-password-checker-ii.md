# 🟠 strong-password-checker-ii — Strong Password Checker II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/strong-password-checker-ii/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Accepted solution for Strong Password Checker II on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        l=u=d=s=False
        sp=set("!@#$%^&*()-+")
        prev=None
        for i in password:
            if i==prev:
                return False
            prev=i
            if i.islower():
                l=True
            elif i.isupper():
                u=True
            elif i.isdigit():
                d=True
            elif i in sp:
                s=True
        return l and u and d and s

```

</details>
