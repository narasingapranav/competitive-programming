# 🟠 find-the-duplicate-number — Find the Duplicate Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Given an array of n + 1 integers where each integer is in the range [1, n], find the single duplicate number.

## 🔍 Key Observation

By storing visited elements in a hash set, the duplicate element can be immediately identified when it is encountered a second time.

## ⚙️ Algorithm

**Hash Set Lookup**

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
    def findDuplicate(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            if i in s:
                return i
            s.add(i)
```

</details>
