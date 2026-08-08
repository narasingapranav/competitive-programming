# 🟠 happy-number — Happy Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/happy-number/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Determine if repeatedly replacing a number with the sum of the squares of its digits eventually leads to 1.

## 🔍 Key Observation

The sequence of digit square sums is bounded and will either terminate at 1 or enter a repeating cycle, which can be detected by storing seen values.

## ⚙️ Algorithm

**Hash set cycle detection**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(log n)` |

## 🏷️ Tags

`hash-table` `math` `cycle-detection`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            su = 0
            for i in str(n):
                su += int(i) ** 2
            n = su
        return n == 1
```

</details>
