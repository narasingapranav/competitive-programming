# 🟠 angle-between-hands-of-a-clock — Angle Between Hands of a Clock

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/) &nbsp;|&nbsp; **Solved:** 2026-06-18

---

## 📝 Summary

Accepted solution for Angle Between Hands of a Clock on LeetCode.

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
    def angleClock(self, hour: int, minutes: int) -> float:
        t=abs(30*hour - 5.5*minutes)
        if t >180:
            return 360-t
        return t
```

</details>
