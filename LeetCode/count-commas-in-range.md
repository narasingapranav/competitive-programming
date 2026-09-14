# 🟠 count-commas-in-range — Count Commas in Range

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-commas-in-range/) &nbsp;|&nbsp; **Solved:** 2026-09-08

---

## 📝 Summary

Count the total number of commas used when formatting all integers from 1 to n with thousands separators.

## 🔍 Key Observation

Numbers strictly below 1000 have no commas, while numbers from 1000 up to 100000 each contain exactly one comma.

## ⚙️ Algorithm

**Math / Case Analysis**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`math` `implementation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        if 1000<=n<=99999:
            return 1+n-1000
        if n==100000:
            return 99001
```

</details>
