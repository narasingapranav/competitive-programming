# 🟠 complement-of-base-10-integer — Complement of Base 10 Integer

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/complement-of-base-10-integer/) &nbsp;|&nbsp; **Solved:** 2026-03-11

---

## 📝 Summary

Accepted solution for Complement of Base 10 Integer on LeetCode.

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
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:]
        rev = ''
        for i in n:
            if i == '1':
                rev += '0'
            else:
                rev += '1'
        return int(rev, 2)
```

</details>
