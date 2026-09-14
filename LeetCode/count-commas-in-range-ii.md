# 🟠 count-commas-in-range-ii — Count Commas in Range II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-commas-in-range-ii/) &nbsp;|&nbsp; **Solved:** 2026-09-10

---

## 📝 Summary

Calculate the total number of commas needed when writing all integers from 1 to n with standard thousands separators.

## 🔍 Key Observation

Numbers in the range [1000^k, 1000^(k+1) - 1] always contain exactly k commas, allowing us to count commas in large logarithmic ranges instead of individually.

## ⚙️ Algorithm

**Math / Range Iteration**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(1)` |

## 🏷️ Tags

`math` `counting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000
        commas = 1
        while start <= n:
            end = min(n, start * 1000 - 1)
            ans += (end - start + 1) * commas
            start *= 1000
            commas += 1
        return ans
```

</details>
