# 🟠 count-commas-in-range — Count Commas in Range

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-commas-in-range/) &nbsp;|&nbsp; **Solved:** 2026-09-08

---

## 📝 Summary

Calculate the total number of commas used when writing all integers from 1 to n in standard comma-separated format.

## 🔍 Key Observation

Numbers in the range [10^(3k), n] contribute an extra comma for each tier of 10^(3k) (1000, 1000000, etc.), so the total count is the sum of max(0, n - 10^(3k) + 1) for all k >= 1.

## ⚙️ Algorithm

**Math / Digit counting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(1)` |

## 🏷️ Tags

`math` `digit-manipulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        if 1000<=n<=100000:
            return 1+n-1000
```

</details>
