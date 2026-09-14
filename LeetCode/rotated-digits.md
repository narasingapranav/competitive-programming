# 🟠 rotated-digits — Rotated Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotated-digits/) &nbsp;|&nbsp; **Solved:** 2026-05-02

---

## 📝 Summary

Accepted solution for Rotated Digits on LeetCode.

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
    def rotatedDigits(self, n: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            isrot = False
            valid = True
            for j in str(i):
                if j in "347":
                    valid = False
                    break
                if j in "2569":
                    isrot = True
            if valid and isrot:
                cnt += 1
        return cnt
```

</details>
