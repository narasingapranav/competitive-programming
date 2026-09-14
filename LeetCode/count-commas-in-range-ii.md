# 🟠 count-commas-in-range-ii — Count Commas in Range II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-commas-in-range-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-09

---

## 📝 Summary

Calculate the total number of commas required to write all integers from 1 to n (inclusive) using standard thousands separators.

## 🔍 Key Observation

The number of commas per integer is constant within intervals defined by powers of 1000 (e.g., 10^3 to 10^6-1 has 1 comma, 10^6 to 10^9-1 has 2 commas), allowing direct constant-time computation for each interval.

## ⚙️ Algorithm

**Math / Range decomposition**

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
