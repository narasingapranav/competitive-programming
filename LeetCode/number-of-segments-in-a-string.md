# 🟠 number-of-segments-in-a-string — Number of Segments in a String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-segments-in-a-string/) &nbsp;|&nbsp; **Solved:** 2025-12-09

---

## 📝 Summary

Accepted solution for Number of Segments in a String on LeetCode.

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
    def countSegments(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        return len(s.split())
```

</details>
