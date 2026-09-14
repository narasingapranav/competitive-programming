# 🟠 excel-sheet-column-title — Excel Sheet Column Title

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/excel-sheet-column-title/) &nbsp;|&nbsp; **Solved:** 2025-08-14

---

## 📝 Summary

Accepted solution for Excel Sheet Column Title on LeetCode.

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
    def convertToTitle(self, columnNumber: int) -> str:
        result = []  
        while columnNumber > 0:
            columnNumber -= 1  
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder)) 
            columnNumber //= 26 
        return "".join(reversed(result))
```

</details>
