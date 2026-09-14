# 🟠 student-attendance-record-i — Student Attendance Record I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/student-attendance-record-i/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Accepted solution for Student Attendance Record I on LeetCode.

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
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        if "LLL" in s:
            return False
        return True
```

</details>
