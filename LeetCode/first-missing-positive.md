# 🟠 first-missing-positive — First Missing Positive

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/first-missing-positive/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Find the smallest missing positive integer in an unsorted array of integers.

## 🔍 Key Observation

The smallest missing positive integer must lie within the range 1 to n + 1, where n is the length of the array.

## ⚙️ Algorithm

**Hash set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`array` `hash-table`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        se = set(nums)
        for i in range(1, n+2):
            if i not in se:
                return i
```

</details>
