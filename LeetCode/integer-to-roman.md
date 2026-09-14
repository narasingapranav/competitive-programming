# 🟠 integer-to-roman — Integer to Roman

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/integer-to-roman/) &nbsp;|&nbsp; **Solved:** 2025-08-24

---

## 📝 Summary

Accepted solution for Integer to Roman on LeetCode.

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
    def intToRoman(self, num: int) -> str:
        roman_symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        roman_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        roman_string = []
        for symbol, value in zip(roman_symbols, roman_values):
            while num >= value:
                num -= value
                roman_string.append(symbol)
        return ''.join(roman_string)
```

</details>
