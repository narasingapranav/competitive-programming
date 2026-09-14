# 🟠 powx-n — Pow(x, n)

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/powx-n/) &nbsp;|&nbsp; **Solved:** 2026-07-22

---

## 📝 Summary

Accepted solution for Pow(x, n) on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`recursion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n&1:
            return x*self.myPow(x*x,n//2)
        return self.myPow(x*x,n//2)
```

</details>
