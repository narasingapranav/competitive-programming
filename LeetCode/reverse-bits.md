# 🟠 reverse-bits — Reverse Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-bits/) &nbsp;|&nbsp; **Solved:** 2026-02-17

---

## 📝 Summary

Accepted solution for Reverse Bits on LeetCode.

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
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            res|= (n & 1) << (31 - i)
            n>>=1
        return res
            
```

</details>
