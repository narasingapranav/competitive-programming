# 🟠 maximum-area-of-longest-diagonal-rectangle — Maximum Area of Longest Diagonal Rectangle

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/) &nbsp;|&nbsp; **Solved:** 2025-09-04

---

## 📝 Summary

Accepted solution for Maximum Area of Longest Diagonal Rectangle on LeetCode.

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
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        l, w = max(
            dimensions,
            key=lambda x: (x[0] * x[0] + x[1] * x[1], x[0] * x[1])
        )
        return l * w
```

</details>
