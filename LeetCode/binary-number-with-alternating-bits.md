# 🟠 binary-number-with-alternating-bits — Binary Number with Alternating Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-number-with-alternating-bits/) &nbsp;|&nbsp; **Solved:** 2026-02-18

---

## 📝 Summary

Accepted solution for Binary Number with Alternating Bits on LeetCode.

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
    def hasAlternatingBits(self, n: int) -> bool:
        x= n^(n>>1)
        return (x & (x+1)) ==0
```

</details>
