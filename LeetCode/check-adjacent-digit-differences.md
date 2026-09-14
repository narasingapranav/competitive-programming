# 🟠 check-adjacent-digit-differences — Check Adjacent Digit Differences

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-adjacent-digit-differences/) &nbsp;|&nbsp; **Solved:** 2026-05-23

---

## 📝 Summary

Accepted solution for Check Adjacent Digit Differences on LeetCode.

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
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) > 2:
                return False
        return True
```

</details>
