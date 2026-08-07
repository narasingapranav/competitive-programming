# 🟠 valid-perfect-square — Valid Perfect Square

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/valid-perfect-square/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Determine whether a given positive integer is a perfect square without using built-in square root functions.

## 🔍 Key Observation

Since the square function is strictly monotonically increasing for positive integers, binary search can be applied on the range [1, num] to locate the integer square root if it exists.

## ⚙️ Algorithm

**Binary search**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(1)` |

## 🏷️ Tags

`binary-search` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        h=num
        while l<=h:
            mid=l+(h-l)//2
            if mid*mid==num:
                return True
            if mid*mid <num:
                l=mid+1
            else:
                h=mid-1
        return False
```

</details>
