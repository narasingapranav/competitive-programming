# 🟠 fibonacci-number — Fibonacci Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/fibonacci-number/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Accepted solution for Fibonacci Number on LeetCode.

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
    def fib(self, n: int) -> int:
        if (n == 0): return 0
        if (n == 1): return 1
        a,b = 0,1
        for i in range(2, n+1):
            a, b = b, a+b
        return b
```

</details>
