# 🟠 minimum-operations-to-equalize-array — Minimum Operations to Equalize Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-array/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Determine the minimum number of operations required to make all elements in an array equal.

## 🔍 Key Observation

If all elements in the array are already identical, 0 operations are needed; otherwise, all elements can be made equal in a single operation.

## ⚙️ Algorithm

**Ad-hoc / Array Inspection**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(1)` |

## 🏷️ Tags

`array` `ad-hoc`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = nums.count(nums[0])
        return 1 if cnt < len(nums) else 0
```

</details>
