# 🟠 zigzag-conversion — Zigzag Conversion

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/zigzag-conversion/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Accepted solution for Zigzag Conversion on LeetCode.

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
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur = 0
        down = False

        for ch in s:
            rows[cur] += ch

            if cur == 0 or cur == numRows - 1:
                down = not down 

            cur += 1 if down else -1

        return "".join(rows)
```

</details>
