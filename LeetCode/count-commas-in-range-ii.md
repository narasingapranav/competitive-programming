# 🟠 count-commas-in-range-ii — Count Commas in Range II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-commas-in-range-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-08

---

## 📝 Summary

Calculate the total number of commas used when formatting all integers from 1 to n with thousand separators.

## 🔍 Key Observation

Numbers within specific digit count ranges (e.g., 4 to 6 digits, 7 to 9 digits) each contain a constant number of commas, allowing direct O(1) mathematical computation based on magnitude ranges.

## ⚙️ Algorithm

**Math / Case Analysis**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        if 1000 <= n <= 999999:
            return 1 + (n - 1000)
        if 1000000 <= n <= 999999999:
            return 2 + 999000 + (n - 1000000) * 2
        if 1000000000 <= n <= 999999999999:
            return 3 + 999000 + 1998000000 + (n - 1000000000) * 3
        if 1000000000000 <= n <= 999999999999999:
            return 4 + 999000 + 1998000000 + 2997000000000 + (n - 1000000000000) * 4
        if n == 1000000000000000:
            return 5 + 999000 + 1998000000 + 2997000000000 + 3996000000000000 

```

</details>
